from src import display as dis
from src import nettoyage as net
from src import recommandation as re
from src import user as user
from src import image as image
import random 
import string 

# (à run 1 fois) Creation des 100 utilisateurs avec leurs préférences 
#user.createUsers()

# Méthode pour mettre les images dans le JSON
net.transform()

#Methodes pour avoir les différents graphique en fonctions des meta données:
#Les graphes sont sauvegardés mais écrasés à chaque relance
dis.DisplayStatType1(10)
dis.DisplayStatType2(10)
dis.DisplayStatTypeImg(10)
dis.DisplayStatTag(10)

#Methode pour avoir la recommandation d'images en fonction de l'utilisateur
re.recommandation(2)
re.recommandation(45)

#Methode pour ajouter un tag à une image
image.add_Tag(1,"vache2")

#methode pour récupérer la liste des images préférées de l'utilisateur
user.getImg_pref(1)

#methode pour ajouter une preférence en plus à l'utilisateur
user.add_preference(1,25)

#methode pour supprimer une préférence
user.remove_preference(1,3)
