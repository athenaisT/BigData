import json
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
import json
import binascii
import struct
import scipy.misc

def ouverture():
    jsonFilePath = r"Data/image.json"
    with open(jsonFilePath, "r") as read_file:
        data = json.load(read_file)
    return data

def write(data):
    with open("Data/image.json", "w") as file:   
       json.dump(data, file)

def add_Tag(idImg, tag):
    data = ouverture()
    tagImg = data[str(idImg)]['Tags']
    tagImg.append(tag)
    data[str(idImg)]['Tags'] = tagImg
    write(data)

def recup_type1(id):
    data = ouverture()
    return data[str(id)]['Type1']

def recup_type2(id):
    data = ouverture()
    return data[str(id)]['Type2']

def recup_tag(id):
    data = ouverture()
    return data[str(id)]['Tags']

def recup_name(id):
    data = ouverture()
    return data[str(id)]['Name']

def recup_typeImg(id):
    
    data = ouverture()
    path = "Images/" +recup_name(id)
    if exists(path+".png"):
        return True
    else:
        return False

# #POur MAx :D
# def remove_Tag(idImg, tag):
#     data = ouverture()
#     tagImg = data[str(idImg)]['Tag']
#     tagImg.remove(tag)
#     data[str(idImg)]['Tag'] = tagImg
#     write(data)

