import arcpy
arcpy.env.overwriteOutput = True

try:
    inPath = arcpy.GetParameterAsText(0)
    outPath = arcpy.GetParameterAsText(1) 
    bufferDistance = arcpy.GetParameterAsText(2)
    
    arcpy.Buffer_analysis(inPath, outPath, bufferDistance)
    
    arcpy.AddMessage("All done") 
    
except:
    arcpy.AddError("Could not complete the buffer")
    
    arcpy.AddMessage(arcpy.GetMessages())