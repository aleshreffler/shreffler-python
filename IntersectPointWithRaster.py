# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 11:26:35 2019

@author: a4kin_000
"""

import arcpy, traceback, sys
##, numpy
from arcpy import env
env.overwriteOutput = True

pntFile=arcpy.GetParameterAsText(0)
rasters=arcpy.GetParameterAsText(1)
rasters=rasters.split(';')
theFields=arcpy.ListFields(pntFile)
theFields=[x.name.lower() for x in theFields]
result=arcpy.GetCount_management(pntFile)
nF=int(result.getOutput(0))
p=arcpy.Point()
try:
    def showPyMessage():
        arcpy.AddMessage(str(time.ctime()) + " - " + message)
    arcpy.AddMessage('\n')
    for raster in rasters:
                desc=arcpy.Describe(raster)
                theFLD=raster.lower()
                arcpy.AddMessage("Sampling "+theFLD)
                if not(theFLD in theFields):
                        arcpy.AddField_management(pntFile, theFLD, "FLOAT")
                arcpy.SetProgressor("step", "", 0, nF)
                with arcpy.da.UpdateCursor(pntFile,("SHAPE@XY",theFLD)) as rows:
                        for row in rows:
                                XY=row[0]
                                p.X,p.Y=XY
                                myArray = arcpy.RasterToNumPyArray(raster,p,1,1,-9999)
                                row[1]=myArray[0,0]
                                rows.updateRow(row)
                                arcpy.SetProgressorPosition()
                        del row,rows
    arcpy.AddMessage('\n')
except NameError, theMessage:
    arcpy.AddMessage (theMessage)
except:
    message = "\n*** PYTHON ERRORS *** "; showPyMessage()
    message = "Python Traceback Info: " + traceback.format_tb(sys.exc_info()[2])[0]; showPyMessage()
    message = "Python Error Info: " +  str(sys.exc_type)+ ": " + str(sys.exc_value) + "\n"; showPyMessage()