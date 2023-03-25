"""
    This code is meant to be copy pasted inside a GhPython component.
    This code is for saving topography's data into a json file.
    Inputs:
            Dump_Json : Boolean to export a JSON file
            Points : list of Point3d of the topography
            Areas : Area of every mesh face of the topography


"""

import os
import Rhino.Geometry as rg
import json

#Create dicts to store the data
X = {}
Y = {}
Z = {}
A = {}

#Loop through the two lists

for i, (pt, area) in enumerate(zip(Points, Areas)):
    X["{}".format(i)] = pt.X
    Y["{}".format(i)] = pt.Y
    Z["{}".format(i)] = pt.Z
    A["{}".format(i)] = area

#Create the dict that will contain all these data and add the data

data = {}
data["X"] = X
data["Y"] = Y
data["Z"] = Z
data["A"] = A

#Locate the current gh folder

gh_canvas = ghenv.Component.OnPingDocument()
folder = os.path.dirname(gh_canvas.FilePath)

#Dump the json file

if Dump_Json:
    with open(os.path.join(folder,'data.json'), 'w') as json_file:
        json.dump(data, json_file, indent = 2)
