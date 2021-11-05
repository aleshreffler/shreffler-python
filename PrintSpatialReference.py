# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 11:08:53 2019

@author: a4kin_000
"""

# Opens a feature class from a geodatabase and prints the spatial reference

import arcpy

featureClass = "C:/GISDATA/WCGIS/GEOG489/Lesson1/USA.gdb/States"

# Describe the feature class and get its spatial reference
desc = arcpy.Describe(featureClass)
spatialRef = desc.spatialReference

# Print the spatial reference name
print spatialRef.Name