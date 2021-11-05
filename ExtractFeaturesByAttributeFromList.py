# Name: ExtractFeaturesByAttributeFromList.py
# Description: Extract features to a new layer where attributes in a given 
# field match at least one value in a given list

# IMPORT SYSTEM MODULES
import arcpy
import sys
import os
from arcpy import env

# DEFINE INPUT VARIABLES
wkSpace = arcpy.GetParameter(0)
csvFile = arcpy.GetParameter(1)
csvField = arcpy.GetParameterAsText(2)
targetLayer = arcpy.GetParameter(3)
targetField = arcpy.GetParameterAsText(4)
outName = arcpy.GetParameter(5)

# SET WORKSPACE AND OVERWRITE PERMISSIONS
env.workspace = wkSpace
env.overwriteOutput = True
outLayer = str(wkSpace) + "\\" + outName + ".shp"
#print(str(outLayer))
arcpy.AddMessage(str(outLayer)) # uncomment if using arcpy

# Write csv list to python list
csvList = [] # list where cursor will write values from csv file
#print(csvField)
arcpy.AddMessage(csvField)
cursor = arcpy.da.SearchCursor(str(csvFile), ["TAXID"]) # establishes cursor
for row in cursor:
    csvList.append(row[0])
#print("List contains " + str(len(csvList)) + " records")
arcpy.AddMessage("List contains " + str(len(csvList)) + " records")

# Use python list to build SQL query
sqlList = ["'" + str(x) + "'" for x in csvList]
#print(sqlList)
arcpy.AddMessage(sqlList)

sqlList = ','.join(sqlList)
#print(sqlList)
arcpy.AddMessage(sqlList)

qry = '"' + str(targetField) + '"' + ' IN (%s)' % sqlList
#print("Executing query: " + str(qry))
arcpy.AddMessage("Executing query: " + str(qry))

# Execute selection tool
arcpy.SelectLayerByAttribute_management(targetLayer, 'NEW_SELECTION', qry)

# Write features to new feature class
#arcpy.CopyFeatures_management(targetLayer, str(outName))
arcpy.Select_analysis(targetLayer, outLayer, qry)

# Print total number of features sucessfully created and matched
result = arcpy.GetCount_management(outLayer)
#print('{} has {} matchable records'.format(outLayer, result[0]))
arcpy.AddMessage('{} has {} matchable records'.format(outLayer, result[0]))
