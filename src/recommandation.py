import json
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.datasets import load_iris
from sklearn import tree
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from src import user as user

def ouverture(path):
    jsonFilePath = path
    with open(jsonFilePath, "r") as read_file:
        data = json.load(read_file)
    return data


# Decision trees, random classifier
def recommandation(idUser):
    dataImg = ouverture("Data/image.json")
    pokemonPref = user.getImg_pref(idUser)   
    index = []
    for row in dataImg :
        index.append(row)
    data = pd.Series(data=dataImg, index=index)
    data["combined_features"] = data.apply(combine_features)
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(data["combined_features"])
    cosine_sim = cosine_similarity(count_matrix) 
    similar = {}
    ind =1
    for i in dataImg :
        similar[str(ind)] = 0
        ind+=1
    for i in pokemonPref :
        similar_img =  list(enumerate(cosine_sim[i]))
        for y in similar_img :
            similar[str(y[0]+1)] += y[1]
    
    fin_max = max(similar, key=similar.get)
    
    similar_img = sorted(similar.items(), key=lambda kv: kv[1])
    #print(similar_img[::-1])
    sorted_similar_img = similar_img[::-1]
    #print (sorted_similar_img)
    i=0
    for element in sorted_similar_img:
            #print(element)
            print (get_title_from_index(dataImg,element[0]))
            i=i+1
            if i>10:
                break
def get_title_from_index(data,index):
    return data[index]["Name"]


def combine_features(row):
        return str(row['Tags']) +" "+ str(row['Type1'])+" "+ str(row["Type2"])+" "+str(row["MainColor"])
