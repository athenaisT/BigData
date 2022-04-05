from ./Data import pref.json
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

#traitement : 
# - like photo -> utilisation crud pref
# - ajout tag -> crud image
#- generation des stats pour les courbes

def Img_pref(numUser):
    with open('pref.json') as pref:
        data_pref = json.load(pref)

    print(data_pref["?"])
    str_pref = json.dumps(data_pref)

    data_dict_02 = json.loads(data_str)
    print(data_dict_02)
    print()

def AjoutTag():
    print()

def GenerationStatColor():
    print()

def GenerationStatType1():
    print()

def GenerationStatType2():
    print()

def GenerationStatTypeImg():
    print()