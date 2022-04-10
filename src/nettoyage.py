from PIL import Image

import numpy as np
import math
import matplotlib.pyplot as plot
from sklearn.cluster import KMeans
from os import listdir
from os.path import isfile, join, exists
import os
import scipy
import scipy.cluster
import pandas as pd
import csv
import random
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
    TagsFilePath = r"Data/Tags.csv" 
        
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
                
                rows['Tags'] = []

                # ajout chemin 
                filepath = "Images/" + rows['Name']

                if exists(filepath+".png") or exists(filepath+".jpg"):
                    if exists(filepath+".png") :
                        rows["FilePath"] = filepath + ".png"
                        rows["typeImg"] = "PNG"
                    else:
                        rows["FilePath"] = filepath + ".jpg"
                        rows["typeImg"] = "JPG"

                    # ajout de la couleur
                    rows["MainColor"] = str(findColor(rows["FilePath"]))

                    # ajout de la ligne dans les données s'il y a une couleur principale
                    if rows["MainColor"] != "" and rows["MainColor"] != None:

                        with open(TagsFilePath, encoding='utf-8') as csvTag:
                            TagsRead = csv.DictReader(csvTag)
                            liste = list(TagsRead)
                            rows['Tags'].append(liste[random.randint(0,len(liste)-1)]['Tag'])
                            rows['Tags'].append(liste[random.randint(0,len(liste)-1)]['Tag'])
                            

                        data[key] = rows
                        numPok+=1
                    else :
                        #removeimage non utilisée
                        clean_img(rows['Name'])
                else:
                    clean_img(rows['Name'])
            else :
                clean_img(rows['Name'])
                #removeimage non utilisée

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

def clean_img(namePokemon):
    path = "Images/" +namePokemon
    if exists(path+".png"):
        path = path + ".png"
        os.remove(path)
    elif exists(path+".jpg"):
        path = path + ".jpg"
        os.remove(path)

