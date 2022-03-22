from PIL import Image

import numpy as np
import math
import matplotlib.pyplot as plot
from sklearn.cluster import KMeans
from os import listdir
from os.path import isfile, join
import scipy
import scipy.cluster
import pandas as pd
import csv
import json

#nettoyage : suppr data not use + mis en forme
# - supression des photos avec que 1 type



#Transformation du csv en JSON
def transform():    
    numPok = 1
    csvFilePath = r'../Data/pokemon.csv'
    jsonFilePath = r'../Data/pokemon.json'
        
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
                # Assuming a column named 'No' to
                # be the primary key
                key = numPok

                data[key] = rows
                numPok+=1

    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))



# Trouver couleur des images ( on prend 2e couleur car sinon c'est le fond)
def findColor():
    mypath = ("../Images")
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    print (onlyfiles)

    NUM_CLUSTERS = 2

    for i in onlyfiles :
        i = mypath + "/" + i

        im = Image.open(i)
        ar = np.asarray(im)
        shape = ar.shape
        ar = ar.reshape(np.product(shape[:2]), shape[2]).astype(float)

        codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)
        print('deuxieme couleur :\n', codes[1])

