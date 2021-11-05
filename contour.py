import arcpy
arcpy.env.overwriteOutput = True

# define local variables
inRaster = "C:/Users/a4kin_000/Documents/ArcGIS/WCGIS/Lesson1/Lesson1/foxlake"
contourInterval = 25
baseContour = 0
outContours = "C:/Users/a4kin_000/Documents/ArcGIS/WCGIS/Lesson1/Lesson1/Lesson1.gdb/FoxLakeContours"

# check out extensions
arcpy.CheckOutExtension("Spatial")
arcpy.CheckOutExtension("3D")

# run contour with messages
try:
    arcpy.Contour_3d(inRaster, outContours, contourInterval, baseContour)
    arcpy.AddMessage("Success!")
    
except:
    arcpy.AddError("Try, try again...")
    
    arcpy.AddMessage(arcpy.GetMessages())