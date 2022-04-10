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


def recommandation(idUser):
    #recuperation de la liste des pokemon et des pokemon preferes de l'utilisateur
    dataImg = ouverture("Data/image.json")
    pokemonPref = user.getImg_pref(idUser)

    # creation d'un tableau pour pouvoir creer une serie panda   
    index = []
    for row in dataImg :
        index.append(row)

    # creation d'une serie panda a partir des donnees de tout les pokemons
    data = pd.Series(data=dataImg, index=index)

    # creation d'une ligne combined fiture un sting qui recence toute 
    # les infos du pokemon sur lesquels on effectue la comparaison
    data["combined_features"] = data.apply(combine_features)

    #print(data)

    cv = CountVectorizer()
    count_matrix = cv.fit_transform(data["combined_features"])
    cosine_sim = cosine_similarity(count_matrix) 

    #initialisation des tableau utilisé pour la recuperation des score de compariason
    similar = {}
    ind = 0
    for i in dataImg :
        similar[str(ind)] = 0
        ind+=1

    # pour on additionne le coeffitient de similarité 
    # obtenu pour chaque pokemon pour chaque pokemon preferé
    for i in pokemonPref :
        similar_img =  list(enumerate(cosine_sim[i-1]))
        for y in similar_img :
            similar[str(y[0])] += y[1]
    
    # recuperation des données dans un tableau
    similar_img = sorted(similar.items(), key=lambda kv: kv[1])

    # invertion du tableau pour obtenir les donnée dans le bon ordre
    sorted_similar_img = similar_img[::-1]
    #print (sorted_similar_img)
    
    # affichage des 10 nom des pokemon les plus similaires aux preferences de l'utilisateur
    i=0
    for element in sorted_similar_img:
            #print(element)
            print (get_title_from_index(dataImg,element[0]))
            i=i+1
            if i>10:
                break

def get_title_from_index(data,index):
    return data[str(int(index)+1)]["Name"]


def combine_features(row):
    # couleur ()
    txt =""
    for i in row['Tags'] :
        txt += i + " "
    txt = txt + str(row['Type1'])+" "+ str(row["Type2"])
    return txt 
