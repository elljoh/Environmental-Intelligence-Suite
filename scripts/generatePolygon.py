## Library dependencies
##!pip install geog
##!pip install shapely

import numpy as np
import json
import geog
import sys
import shapely.geometry

# Mandatory args: lat, lon
# Optional arg: FieldName; if not provided, will be constructed using lat/lon
# Example: python generatePolygon -101.162714000941 41.0464218322353 field-A
if (len(sys.argv) < 3 or len(sys.argv) > 4):
    print ('Usage: generatePolygon.py <latitude> <longitude> [FieldName]')
    sys.exit()

lat = float (sys.argv[1])
lon = float (sys.argv[2])

print (len(sys.argv))

if (len(sys.argv) == 4):
    fileName = sys.argv[3] + ".json"
else:
    fileName = "Field_" + str(((int)(lat * 100) * 1000) + (int)(lon * 100)) + ".json"

## Constants
d = 1000  # radius in meters
n_points = 20  # of points in the polygon

p = shapely.geometry.Point([lat,lon])
angles = np.linspace(0, 360, n_points)
polygon = geog.propagate(p, angles, d)
shapelyPolygon = shapely.geometry.mapping(shapely.geometry.Polygon(polygon))
features = [{'type': 'Feature', 'properties': {}, 'geometry': shapelyPolygon}]
featureCollection = {"type": "FeatureCollection", "features": features}
print(json.dumps(featureCollection))
with open(fileName, 'w') as outfile:
    json.dump(featureCollection, outfile)
