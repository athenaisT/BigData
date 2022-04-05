from PIL import Image

import numpy as np
import math
import matplotlib.pyplot as plot
from sklearn.cluster import KMeans
from os import listdir
from os.path import isfile, join, exists
import scipy
import scipy.cluster
import pandas as pd
import csv
import json
import binascii
import struct
import scipy.misc

#nettoyage : suppr data not use + mis en forme
# - supression des photos avec que 1 type



#Transformation du csv en JSON
def transform():    
    numPok = 1
    csvFilePath = r"Data/pokemon.csv" 
    jsonFilePath = r"Data/image.json"
        
    # create a dictionary
    data = {}

    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
            
            #on ne recupere que les pokemon avec 2 types
            if rows.get('Type2') != None: 
                # on ajoute numPok pour avoir un numero comme clé 
                key = numPok
                
                rows['Tags'] = ""

                # ajout chemin 
                filepath = "Images/" + rows['Name']

                if exists(filepath+".png"):
                    rows["FilePath"] = filepath + ".png"
                else:
                    rows["FilePath"] = filepath + ".jpg"

                # ajout de la couleur
                rows["MainColor"] = str(findColor(rows["FilePath"]))

                # ajout de la ligne dans les données s'il y a une couleur principale
                if rows["MainColor"] != "":
                    data[key] = rows
                    numPok+=1

    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))



# Trouver couleur des images ( on prend la 2e couleur car sinon c'est le fond)
def findColor(Path):
    # print (Path)

    if exists(Path) :
        try:
            NUM_CLUSTERS = 2

            im = Image.open(Path)
            ar = np.asarray(im)
            shape = ar.shape
            ar = ar.reshape(np.product(shape[:2]), shape[2]).astype(float)

            codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)
            # print('deuxieme couleur :\n', codes[1])
            return codes[1]
        except :
            return ""

