# SCRIPT NAME: Separate Shapefile by Type Attribute
# DESCRIPTION: This script makes a separate shapefile for each type of amenity from a single feature class within the boundary of El Salvador.
# WRITTEN BY: Alexandria Shreffler

import arcpy

# Allow the overwriting of outputs
arcpy.env.overwriteOutput = True

# Step 1: Define workspace, paths, and variables
arcpy.env.workspace = "C:/Users/a4kin_000/Documents/ArcGIS/WCGIS/GEOG485/Lesson3/Project3"
featureClass = "OSMpoints.shp"
boundaries = "CentralAmerica.shp"
amenities = ['place_of_worship','hospital','school']
country = 'El Salvador'
nameField = "NAME"

# Step 2: Prepare before the amenity selection loop
# Create a layer for the country boundary to be used in the loop 
arcpy.MakeFeatureLayer_management(boundaries,"SelectionCountryLayer",'"' + str(nameField) + '" =' + "'" + str(country) + "'")

# Create a list for reporting created datasets
created = []

# Step 3: Create a separate shapefile for each type of amenity using a loop
try:
    for amenity in amenities: 
        # Create a statement which selects records with each amenity
        amenitySelectionClause = '"amenity" = ' + "'" + amenity + "'"

        # Select each amenity and make a new layer
        arcpy.MakeFeatureLayer_management(featureClass, "Selection" + amenity + "Layer", amenitySelectionClause)

        # Select only within the country boundary 
        arcpy.SelectLayerByLocation_management("Selection" + amenity + "Layer","WITHIN","SelectionCountryLayer")

        # Save each layer as a feature class
        arcpy.CopyFeatures_management("Selection" + amenity + "Layer", amenity)

        # Add to list of created datasets
        created.append(amenity)

        # Delete the amenity layer once saved as shapefile
        arcpy.Delete_management("Selection" + amenity + "Layer")

        # Add a text field named "source" and populate with "OpenStreetMap"
        arcpy.AddField_management(amenity + ".shp", "source", "TEXT")
        with arcpy.da.UpdateCursor(amenity + ".shp", ("source",)) as cursor:
            for row in cursor:
                row[0] = "OpenStreetMap"
                cursor.updateRow(row)

    # Print the list of created datasets
    print "Created new files for " + ", ".join(str(fC) for fC in created)

except:
    # Report error
    arcpy.AddError("Could not complete task.")

    # List messages
    arcpy.GetMessages()