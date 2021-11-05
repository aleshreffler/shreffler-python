# This script clips all datasets in a folder
import arcpy
 
inFolder = "c:\\data\\inputShapefiles\\"
resultsFolder = "c:\\data\\results\\"
clipFeature = "c:\\data\\states\\Nebraska.shp"
 
# List feature classes
arcpy.env.workspace = inFolder
featureClassList = arcpy.ListFeatureClasses()
 
# Loop through each feature class and clip
for featureClass in featureClassList:
     
    # Make the output path by concatenating strings
    outputPath = resultsFolder + featureClass <----
    # Clip the feature class
    arcpy.Clip_analysis(featureClass, clipFeature, outputPath)
