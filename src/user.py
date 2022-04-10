import json

#read create
import random
from re import S 
import string 
from src import image as image

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
    
def createUsers():
    jsonFilePath = r"Data/user.json"
    
        
    # create a dictionary
    #new = numUser
    data = None
    
    # 1. Read file contents
    with open(jsonFilePath, "r") as read_file:
        data = json.load(read_file)
    # 2. Update json, object
    for i in range (100):
        prenom = get_random_string(5)
        row = {}
        row['Name'] = prenom
        row['Num'] = i + 1 
        row['Preference']=[]
        for j in range (0,20):
            imgs=image.ouverture()
            total=len(imgs) 
            row['Preference'].append(random.randint(1,total))
        data[i+1] = row
  #     # 3. Write json file 
  
    with open(jsonFilePath, "w") as file:
       
       json.dump(data, file)


def ouverture():
    jsonFilePath = r"Data/user.json"
    with open(jsonFilePath, "r") as read_file:
        data = json.load(read_file)
    return data

def write(data):
    with open("Data/user.json", "w") as file:   
       json.dump(data, file)


def add_preference(idUser, idImage):
    data = open()
    prefUser = data[str(idUser)]['Preference']
    prefUser.append(idImage)
    data[str(idUser)]['Preference'] = prefUser
    write(data)


def remove_preference(idUser, idImage):
    data = ouverture()
    prefUser = data[str(idUser)]['Preference']
    prefUser.remove(idImage)
    data[str(idUser)]['Preference'] = prefUser
    write(data)

def getImg_pref(id_user):
    data =ouverture()
    prefUser = data[str(id_user)]['Preference']
    return prefUser