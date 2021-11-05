# SCRIPT NAME: Compare Feature Class Statistics
# DESCRIPTION: This script creates compares the statistics of two feature classes and produces a feature class as a output with results. 
# WRITTEN BY: Alexandria Shreffler

# Import modules
import arcpy
import csv

# Overwrite outputs
arcpy.env.overwriteOutput = True

# Define variables, retrieve from parameter inputs
workspace = arcpy.GetParameterAsText(0)
fieldInput = arcpy.GetParameterAsText(1)
compareInput  = arcpy.GetParameterAsText(2)
spatialInput  = arcpy.GetParameterAsText(3)
idField = arcpy.GetParameterAsText(4)
output = arcpy.GetParameterAsText(5)

# Create a feature layer out of the spatial input in order to copy features
arcpy.SaveToLayerFile_management(spatialInput, spatialLayer)

# Copy features from spatial input and place in new feature class
arcpy.CopyFeatures_management(spatialLayer, output)

# Add statistical fields to the output layer
arcpy.AddField_management(output, "SUM", "FLOAT")
arcpy.AddField_management(output, "AVE", "FLOAT")
arcpy.AddField_management(output, "SD", "FLOAT")

try:
# Check for identifying field name in all feature classes
    fieldList = arcpy.ListFields(fieldInput) # Lists fields in first feature class
    if idField in fieldList: # Checks fields in first feature class
        arcpy.AddMessage("Identifying field confirmed in " + fieldInput)
    else: 
        arcpy.AddMessage("Identifying field absent in " + fieldInput)

    compareList = arcpy.ListFields(compareInput) # Lists fields in second feature class
    if idField in compareList: # Checks fields in second feature class
        arcpy.AddMessage("Identifying field confirmed in " + compareInput)
    else: 
        arcpy.AddMessage("Identifying field absent in " + compareInput)

    spatialList = arcpy.ListFields(spatialInput) # Lists fields in the spatial feature class
    if idField in spatialInput: # Checks fields in spatial feature class
        arcpy.AddMessage("Identifying field confirmed in " + spatialInput)
    else:
        arcpy.AddMessage("Identifying field absent in " + spatialInput)

except: 
    arcpy.AddMessage("Error processing data inputs")

try:
# Create a dictionary for referencing records in the second field list
    compareCursor = arcpy.da.SearchCursor(compareInput, ['idField', compareList])
    compareDict = {row[0]:(row[1:]) for row in compareCursor} 
# Check all fields for numeric values and presence in both datasets
    for field in fieldList: # initiate loop for fields in the first list
        arcpy.AddMessage("Discovering " + field)
        if field.isnumeric() == True: # check if field is numerical
            arcpy.AddMessage(field + " is numerical")
            if field in compareList:
                arcpy.AddMessage(field + " confirmed in " + compareList)
                arcpy.AddMessage("calculating statistics for " + field)
                # match ID?
                with arcpy.da.SearchCursor(fieldInput, ['idField', field]) as cursor:
                    for row in cursor:
                        arcpy.AddMessage("ID " + row[0] + "selected")
                        key = row[0]
                        if key in compareDict: # THIS IS WHERE I STARTED TO GET STUCK

                        else:
                            arcpy.AddMessage("ID not found in comparison data")
                            continue
                # report "statistics for <field> calculated" for each field
            else:
                arcpy.AddMessage(field + " absent from " + compareList)
                continue
        else:
            arcpy.AddMessage(field + " is not numerical")
            continue