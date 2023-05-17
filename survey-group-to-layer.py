import arcpy
# this script will find find within the current project a map defined with MAP_NAME, and
# then merge all the points and polyline data found within the SURVEY_LAYER 
# into two distinct layers - one for Points and the other Polylines


# layer structure
# Map
# -> KI Cave Survey Data
#    -> K<something>
#       -> Points
#       -> Polylines

# set this value to be wherever the gdb is located
PROJECT_PATH = "C:\\Users\\Matt\\Documents\\SASC GIS Project\\SASC GIS Project\\"
PROJECT_GDB = "SASC GIS Project.gdb"
MAP_NAME = "Map"
SURVEY_LAYER = "KI Cave Survey Data"

OUT_POINTS_GBD = r"KI Survey All Stations.gdb"
OUT_POINTS = "ki_survey_all_stations"

OUT_POLYLINES_GBD = r"KI Survey All Legs.gdb"
OUT_POLYLINES = "ki_survey_all_legs"

# Create a new geodatabase for the merged output
arcpy.management.CreateFileGDB(PROJECT_PATH, OUT_POINTS_GBD)
arcpy.management.CreateFileGDB(PROJECT_PATH, OUT_POLYLINES_GBD)

aprx = arcpy.mp.ArcGISProject("CURRENT")
aprx.defaultGeodatabase = PROJECT_PATH + PROJECT_GDB

# get the map
m = aprx.listMaps(MAP_NAME)[0]

# assumption - there's a map called "KI Cave Survey Data"!
ki_survey_layer = m.listLayers(SURVEY_LAYER)[0]

# Create a list to hold the point and polyline layer items
point_classes = []
polyline_classes = []

# Iterate over the layers within the group layer
for layer in ki_survey_layer.listLayers("Points"):
    point_classes.append(layer.dataSource)

for layer in ki_survey_layer.listLayers("Polylines"):
    polyline_classes.append(layer.dataSource)


arcpy.management.Merge(point_classes, "{}/{}".format(OUT_POINTS_GBD, OUT_POINTS))  
arcpy.management.Merge(polyline_classes, "{}/{}".format(OUT_POLYLINES_GBD, OUT_POLYLINES))  
