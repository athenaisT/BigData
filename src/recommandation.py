
import json
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.datasets import load_iris
from sklearn import tree
import matplotlib.pyplot as plt
import pandas as pd
import pydotplus
from src import user as user
from sklearn.metrics.pairwise import cosine_similarity

def ouverture(path):
    jsonFilePath = path
    with open(jsonFilePath, "r") as read_file:
        data = json.load(read_file)
    return data

# Decision trees, random classifier
def recommandation(idUser):
    dataImg = ouverture("Data/image.json")
    pokemonPref = user.getImg_pref(idUser)
    infoPref = []

    for i in pokemonPref:
        infoPref.append(dataImg[str(i)])

    #print("poke",pokemonPref)
    #print ("info",infoPref)
    
    
    
    #truc github
    features = ['Tags','Type1','Type2','MainColor']

    index = []

    for row in dataImg :
        index.append(row)

    data = pd.Series(data=dataImg, index=index)

    data["combined_features"] = data.apply(combine_features)

    cv = CountVectorizer()
    count_matrix = cv.fit_transform(data["combined_features"])
    cosine_sim = cosine_similarity(count_matrix) 

    similar_img =  list(enumerate(cosine_sim[pokemonPref]))
    
    #similar_img.sort_values(ascending=True)

    sorted_similar_img = sorted(similar_img,key=lambda x:x[0],reverse=True)[1:]
    test=[similar_img,sorted_similar_img]
    print("tst",test)
    i=0
    for element in sorted_similar_img:
        print (get_title_from_index(data,element[0]))
        i=i+1
        if i>50:
            break

def get_title_from_index(data,index):
	return data[index]['Name']

def combine_features(row):
        return str(row['Tags']) +" "+ str(row['Type1'])+" "+ str(row["Type2"])+" "+str(row["MainColor"])

    

        





    # d = {'UK': 0, 'USA': 1, 'N': 2}
    # data['Name'] = data['Num'].map(d)
    # d = {'YES': 1, 'NO': 0}
    # data['Go'] = data['Go'].map(d) 
    # features = ['Age', 'Experience', 'Rank', 'Nationality']

    # X = data[features]
    # y = data['Go']

    # dtree = DecisionTreeClassifier()
    # dtree = dtree.fit(X, y)
    # data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
    # graph = pydotplus.graph_from_dot_data(data)
    # graph.write_png('mydecisiontree.png')

    # img=plt.imread('mydecisiontree.png')
    # imgplot = plt.imshow(img)
    # plt.show()     
    
   

