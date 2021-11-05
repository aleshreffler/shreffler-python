# SCRIPT NAME: Create Polylines from Coordinate Observations
# DESCRIPTION: This script creates polyline features from a list of observationed coordinates.
# WRITTEN BY: Alexandria Shreffler

# Step 1: Prepare for scripting. 
# Create a function to add a polyline 
def addPolyline(cursor, array, sr):
    polyline = arcpy.Polyline(array, sr)
    cursor.insertRow((polyline,))

# Import the modules. 
import arcpy 
import csv

# Set workspace
arcpy.env.workspace = "C:/Users/a4kin_000/Documents/ArcGIS/WCGIS/GEOG485/Lesson4"

# Allow overwriting
arcpy.env.overwriteOutput = True

# Create spatial reference object for polyline feature class
# Geographic Coordinate system "WGS 1984" (factory code=4326)
# spatialRef = arcpy.SpatialReference("WGS 1984") # I was unable to call this object in the CreateFeatureclass tool, so I just called the spatial reference in the tool, which seemed to work...

# Create the feature class for the polylines
arcpy.CreateFeatureclass_management(arcpy.env.workspace,"RhinoObservations.shp","POLYLINE","","","","WGS 1984")

# Set up variables: 
observations = open("C:/Users/a4kin_000/Documents/ArcGIS/WCGIS/GEOG485/Lesson4/RhinoObservations.csv")
polylineFC = "RhinoObservations.shp"

# Create empty list of names and arrays and a dictionary which pairs them together
nameList = []
arrayList = []
nameCoord = {}

# Set up csv reader
csvReader = csv.reader(observations)

# Process header 
header = csvReader.next()

# Define lat/long/name
latIndex = header.index("X")
lonIndex = header.index("Y")
nameIndex = header.index("Rhino")

# Step 2: Use the spreadsheet to generate a dictionary of coordinates with cooresponding names. 
# Loop through the header to find the index position of the name, X (lat), and Y (long) values. 
for row in csvReader:
    lat = row[latIndex]
    lon = row[lonIndex]
    name = row[nameIndex]
    # Add name to list of names
    nameList.append(name)
    # Create a loop that makes an array for each name
    arrayList = [[arcpy.Array()] for _ in range(len(nameList))]
    # Pair names and arrays in a dictionary
    nameCoord = dict(zip(nameList, arrayList))
    print nameCoord
# Check if the name is listed as a key in the dictionary.
for row in csvReader:
    for name, value in nameCoord.iteritems():
        # Create a new point object.
        vertex = arcpy.Point(lon,lat)
        # Add it to the appropriate array.
        value.add(vertex)
        # Check entry by printing
        print str(value) + " belongs to " + name
# Step 3: Create a polyline feature with the list of coordinates.
for name, value in nameCoord.iteritems():
    # Write the array to the feature class as a polyline feature.
    with arcpy.da.InsertCursor(polylineFC, ("SHAPE@",)) as cursor:
        addPolyline(cursor, value, "WGS 1984")