import arcpy
arcpy.env.overwriteOutput = True
from arcpy.sa import *

inRaster = "C:/Users/a4kin_000/Documents/ArcGIS/WCGIS/Lesson1/Lesson1/foxlake"
cutoffElevation = 2500

arcpy.CheckOutExtension("Spatial")

outRaster = Raster(inRaster) > cutoffElevation
outRaster.save("C:/Users/a4kin_000/Documents/ArcGIS/WCGIS/Lesson1/Lesson1/foxlake_hi_10")

arcpy.CheckInExtension("Spatial")