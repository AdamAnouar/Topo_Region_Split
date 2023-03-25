"""
    Gaussian Mixture CLustering using sklearn and Pandas libraries
    This code is meant to run outside of the Rhino Grasshopper environment
    and with the compatible CPython version. 

"""


import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.mixture import GaussianMixture
import os
import json


    
#Clustering using GaussianMixture


#Find the folder path (always place this python file in the same folder as the gh file)
Folder_path = os.path.dirname(__file__)
full_path = os.path.join(Folder_path,"data.json")
topography = pd.read_json(full_path)
topography.head()

#In case more features are added, we isolate those we need
features = ["X","Y","Z","A"]
X = topography[features]
Z = StandardScaler()
X[features] = Z.fit_transform(X)
EM = GaussianMixture(n_components=3)
EM.fit(X)
cluster = EM.predict(X)
X["cluster"] = cluster

#Save labels in a Dict
clustered_data = {}
for index, row in X.iterrows():
    clustered_data['cluster'] = row

#Define the file_path 
full_path = os.path.join(Folder_path,"cluster_data.json")

#Export Json
X.to_json(full_path)

