# TOOL NAME: Conduct Multi-Classification Accuracy Assessment Comparison

# DESCRIPTION: This script simplifies the process of conducting an accuracy assessment on more than one landcover classification method.
#               This accuracy assessment includes comparing classification results to ground truthed points and computing error matrices.It also
#               reports the relevant statistics, including the overall accuracy (%) of each classification and identifies the most inaccurate classes.
#               Finally, a layer of misclassified points is produced which can be used to verify accurate ground truthing and classification results.

# REQUIREMENTS: Prior to running this script, the user should have already run the Create Accuracy Assessment Points geoprocessing tool
#               and updated the 'GrndTruth' field with ground truthed information. This script also requires that assessment classifications
#               be located in a single file geodatabase with the first five characters being unique in each file name. Finally, the classes for each
#               classification (and the ground truthed points) must be standardized using numerical values.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# IMPORT MODULES:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os

import arcpy
from arcpy.sa import *
from pandas_ml import ConfusionMatrix # Install this module: pip install pandas_ml
import xlsxwriter # Install this module: pip install XlsxWriter


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# DEFINE USER INPUT AND RELATED VARIABLES:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Ground Truth Points:
#grndTruth = "C:\\GISDATA\\WCGIS\\GEOG489\\FinalProject\\MyProject\\Data.gdb\\GroundTruthPoints"
grndTruth = arcpy.GetParameterAsText(0)               # ground truth points; also shares the save location for the (in)accuracy point feature classes

# Classifications to be assessed
#toBeAssessed = "C:\\GISDATA\\WCGIS\\GEOG489\\FinalProject\\MyProject\\Classifications.gdb"
toBeAssessed = arcpy.GetParameterAsText(1)            # geodatabase must contain only the classifications to be assessed
classFieldNames = []        # for storing classification field names

#pointLocation = "C:\\GISDATA\\WCGIS\\GEOG489\\FinalProject\\MyProject\\Points.gdb" # this will be created if it does not already exist
pointLocation = arcpy.GetParameterAsText(2)                 # location where the classification point layer geodatabase will be stored
pointLayers = []            # list for storing resulting feature classes


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Prepare for accuracy assessment:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# set overwriting
arcpy.env.overwriteOutput = True

# Check out Spatial Analyst Extension (Extract Values to Points)
arcpy.CheckOutExtension("Spatial")

try:
#    print("Preparing for accuracy assessment...")
    arcpy.AddMessage("Preparing for accuracy assessment...")
    # Create the point geodatabase
    pointBase = "Point.gdb"
    arcpy.CreateFileGDB_management(pointLocation, pointBase)
    pointGDB = pointLocation + "\\" + pointBase
    arcpy.AddMessage(str(pointBase) + " geodatabase created.")

    # Copy grndTruth to new point layer: AssessmentPoints
    grndDir = os.path.dirname(grndTruth)
    arcpy.env.workspace = grndDir
    arcpy.Copy_management(grndTruth, "\\AssessmentPoints")
    arcpy.DeleteField_management("AssessmentPoints", ["Classified"]) # Delete the existing "Classified" field
    grndTruthIndex = 2 # new index of the field containing the ground truth values

    # List the feature classes in the classifications geodatabase
    arcpy.env.workspace = toBeAssessed
    featureClasses = arcpy.ListFeatureClasses()
    rasters = arcpy.ListRasters()
    numClass = len(featureClasses) + len(rasters)
    #print("Assessing " + str(numClass) + " classifications:")
    #print("Feature Classes: " + str(featureClasses))
    #print("Rasters: " + str(rasters))

    # Variables related to the final assessment point feature class:
    finalFieldIndices = [] # index list
    finalFieldObjects = [] # field objects
    finalFieldNames = [] # field names
    classFieldIndex = [] # index list for classification fields
    pointDict = {} # dictionary linking the name of the classification with the

except:
#    print("Error: Unable to prepare for accuracy assessment...")
    arcpy.AddMessage("Error: Unable to prepare for accuracy assessment...")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Get classification values at ground truth points:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
arcpy.AddMessage("STEP 1: Get Classification Values at Ground Truth Points")

try:
    # FEATURE CLASS PROCESSING: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#    print("Identifying point values in feature classes...")

    arcpy.AddMessage("Identifying point values in feature classes...")
    idFeatures = grndDir + "\\AssessmentPoints"
    for inFeatures in featureClasses:
        name = arcpy.Describe(inFeatures).baseName
        shortName = name[:6] if len(name) > 10 else name
        upName = shortName.upper()

#        print("Processing: {0} will be represented in field {1}".format(name, upName))
        arcpy.AddMessage("Processing Classification Feature Class: {0} will be represented in field {1}".format(name, upName))

        classFieldNames.append(upName)
        outFeatures = pointGDB + "\\" + shortName + "Points"
        arcpy.SpatialJoin_analysis(idFeatures, inFeatures, outFeatures)

        # Manage fields in output in order to correctly refer to them by index later in the confusion matrix code
        outFields = arcpy.ListFields(outFeatures)
        for f in outFields:
            if f.name == "Value":
                arcpy.AlterField_management(outFeatures, f.name, str(upName), str(upName)) # Rename "Value" field after name of feature class
            elif f.name == "Join_Count":
                arcpy.DeleteField_management(outFeatures, f.name)
            elif f.name == "TARGET_FID":
                arcpy.DeleteField_management(outFeatures, f.name)
            elif f.name == "GrndTruth":
                arcpy.DeleteField_management(outFeatures, f.name)
            else:
                pass
#            print("Feature Class Field:      {0}".format(f.name))

    # RASTER PROCESSING:~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#    print("Extracting raster values to points...")
    arcpy.AddMessage("Extracting raster values to points...")
    for inRaster in rasters:
        name = arcpy.Describe(inRaster).baseName
        shortName = name[:6] if len(name) > 10 else name
        upName = shortName.upper()
#        print("Processing: {0} will be represented in field {1}".format(name, upName))
        arcpy.AddMessage("Processing Classification Raster: {0} will be represented in field {1}".format(name, upName))
        classFieldNames.append(upName)
        outFeatures = pointGDB + "\\" + shortName + "Points"
        ExtractValuesToPoints(idFeatures, inRaster, outFeatures) # Extract Values to Points
        outFields = arcpy.ListFields(outFeatures)
        for f in outFields:
            if f.name == "RASTERVALU":
                arcpy.AlterField_management(outFeatures, f.name, str(upName), str(upName)) # Rename "Value" field after name of feature class
            elif f.name == "GrndTruth":
                arcpy.DeleteField_management(outFeatures, f.name)
            else:
                pass
#            print("Raster Field:      {0}".format(f.name))

except:
#    print("Error: Unable to intersect classifications with ground truth information...")
    arcpy.AddMessage("Error: Unable to intersect classifications with ground truth information...")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Merge data by linking back to copy:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Set workspace:
arcpy.env.workspace = pointGDB
try:
    # Prepare for merging
#    print("Joining accuracy assessment points...")
    arcpy.AddMessage("Joining accuracy assessment points...")

    pointLayers = arcpy.ListFeatureClasses()

    # Join tables to common field, OBJECTID
    final = grndDir + "\\AssessmentPoints"
    for layer in pointLayers:
        arcpy.JoinField_management(final, "OBJECTID", layer, "OBJECTID")
    listFinalFields = arcpy.ListFields(final)

    # Some formatted result information:
    result = arcpy.GetCount_management(final)
#    print('{} records have been found.'.format(result[0]))
    arcpy.AddMessage('{} records have been found.'.format(result[0]))

    for field in listFinalFields:
#        print("Final Field:        {0}".format(field.name))
        finalFieldNames.append(str(field.name))
    arcpy.AddMessage("Sucess: Assessment Point feature class contains classification value information...")

except:
#    print("Error: Unable to link classification value information to ground truth data...")
    arcpy.AddMessage("Error: Unable to link classification value information to ground truth data...")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Compute confusion matrices and statistics:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
arcpy.AddMessage("STEP 2: Compute Confusion (Error) Matrices and Statistics")

# Create workbook
workbookPath = pointGDB + "\\ErrorMatrices.xlsx"
workbook = xlsxwriter.Workbook(workbookPath)
bold = workbook.add_format({'bold': True})
#red = workbook.add_format({'font_color': 'Red'})

# Set workspace:
arcpy.env.workspace = pointGDB

# Define characteristics of the AssessmentPoints in order to access the field values
classFieldIndices = [x + grndTruthIndex + 1 for x in range(len(classFieldNames))]
pointDict = dict(zip(classFieldNames, classFieldIndices))

try:
#    print("Computing matrices and creating workbook...")
    arcpy.AddMessage("Computing matrices and creating workbook...")

    # Compute maxtrices and write to workbook
    reference = []
    classified = []
    for name in pointDict: # loop through the index of the point layer to generate a confusion matrix for each classified field list
        with arcpy.da.SearchCursor(final, finalFieldNames, None) as cursor:
            reference = [row[grndTruthIndex] for row in cursor] # lists the ground truth values in a list
            cursor.reset()
            classified = [row[pointDict[name]] for row in cursor] # lists the classified values in a list
#            print(str(reference[0:11]))
#            print(str(classified[0:11]))
        cm = ConfusionMatrix(classified, reference)

        cm.print_stats()
        arcpy.AddMessage(str(cm._str_stats())) # Report statistics for the matrix

        worksheet = workbook.add_worksheet(name) # create a new worksheet for this matrix

        # Prepare to write CM data to the XLSX worksheet
        cmDataframe = cm.to_dataframe()
        cmRows = len(cmDataframe) # number of rows (classified classes)
        cmRowIndices = range(cmRows)
        cmColumns = len(cmDataframe.columns) # number of columns (reference classes)
        cmColumnIndices =  range(cmRows)
        print(cmDataframe)
        print("Rows: " + str(cmRows))
        print("Columns: " + str(cmColumns))
        print("Rows: " + str(cmRowIndices) + " Columns: " + str(cmColumnIndices))

        # Apply general formatting rules to XLSX worksheet
        worksheet.set_row(0, None, bold)
        worksheet.set_column('A:A', None, bold)

        writeResults = 0 # should remain 0 if successful
        # Write class names to worksheet
        cmClassList = cmDataframe.columns
        cmClassIndices = [x+1 for x in range(len(cmClassList))]
        cmClassDict = dict(zip(cmClassList, cmClassIndices))
#        print(cmClassList)
#        print(cmClassIndices)
#        print(cmClassDict)
        for n in cmClassDict:
            result = worksheet.write(0, cmClassDict[n], n)
            writeResults += result
            result = worksheet.write(cmClassDict[n], 0, n)
            writeResults += result

        # Write the CM results to the workbook:
        for r in cmRowIndices:
            for c in cmColumnIndices:
                content = cmDataframe.iloc[r, c]
                xlsxR = r+1
                xlsxC = c+1
                result = worksheet.write_number(xlsxR, xlsxC, content)
                writeResults += result
#                print(str(content))
        if writeResults == 0:
            arcpy.AddMessage("Successfully added all content to worksheet...")
        else:
            arcpy.AddMessage("Warning: Something may not have been written correctly to ErrorMatrices.xlsx")

except:
#    print("Error: Unable to create matrices...")
    arcpy.AddMessage("Error: Unable to create matrices...")

workbook.close()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Generate a layer of mis-classified points
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Set workspace:
arcpy.env.workspace = pointGDB

arcpy.AddMessage("STEP 3: Generate Inaccuracy Points")

try:
    #print("Creating inaccuracy points...")
    arcpy.AddMessage("Creating inaccuracy points...")

    # Add field to pointOutput feature class called "MATCH"
    arcpy.AddField_management(final, "MATCH", "TEXT", 15)
    listFinalFields = arcpy.ListFields(final)
    finalFieldNames = [field.name for field in listFinalFields] # updates list of names
    finalFieldIndices = [x for x in range(len(finalFieldNames))] # updates index values for list of names
    #print(finalFieldIndices)
    matchIndex = finalFieldIndices[-1] # gets the index of the last field in the table, which is the recently created one
    #print(matchIndex)

    # Set the default value of the match field to "ALL"
    with arcpy.da.UpdateCursor(final, finalFieldNames) as cursor:
        for row in cursor:
            row[matchIndex] = "YES" # default value of "MATCH will be "ALL"
            cursor.updateRow(row)
    del row, cursor
    #print("'MATCH' field created. Default value 'ALL' set.")
    arcpy.AddMessage("'MATCH' field created. Default value 'YES' set.")

    # loop through the classified fields of the point layer to check whether they match the reference field
    #print("Checking whether classified field values match the ground truth values...")
    arcpy.AddMessage("Checking whether classified field values match the ground truth values...")
    for name in pointDict:
        with arcpy.da.UpdateCursor(final, finalFieldNames) as cursor:
            for row in cursor:
                if row[matchIndex] == "YES":
                    if row[pointDict[name]] != row[grndTruthIndex]: # if classified field value does not equal reference field value
                        row[matchIndex] = "NO" # change "MATCH" field to "NO"
                        cursor.updateRow(row)
                    else:
                        pass
                else:
                    pass
        del row, cursor

    # Select features in pointOutput using match field to create inaccuracy layer
    query = '"MATCH" <> \'YES\''
    outPoints = grndDir + "\\InaccuracyPoints"
    arcpy.Select_analysis(final, outPoints, query)

#    print("Success: Inaccuracy points created.")
    arcpy.AddMessage("Success: Inaccuracy points created.")

except:
#    print("Error: Unable to create inaccuracy points...")
    arcpy.AddMessage("Error: Unable to create inaccuracy points...")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Clean-up code:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\
# Check in Spatial Analyst Extension
arcpy.CheckInExtension("Spatial")
