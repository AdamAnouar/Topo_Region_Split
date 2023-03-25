"""
    This code is meant to be copy pasted inside a GhPython component.
    This code is for loading clustered topography's data from a json file.
    Inputs:
            Read : Boolean to load clustered data from the JSON file
    Outputs:
            Indices : The index of every point in the topography
            Cluster_labels : Integer representing the cluster number

"""

import json
import Rhino.Geometry as rg
import os

#Get current Directory
gh_canvas = ghenv.Component.OnPingDocument()
folder = os.path.dirname(gh_canvas.FilePath)


#Load Json
if Read:
    with open(os.path.join(folder, 'cluster_data.json')) as file:
        Clustered = json.load(file)

#Isolate the labels
    Labels = Clustered['cluster']

    Indices = []
    Cluster_labels = []
#Append in output lists
    for key, value in Labels.items():
        Indices.append(key)
        Cluster_labels.append(value)


