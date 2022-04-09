from src import display as dis
from src import nettoyage as net
from src import recommandation as re
from src import user as user
import random 
import string 

# git push https://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@github.com/athenaisT/BigData.git

#dis.menu()
#net.transform()
#user.getImg_pref(1)
#dis.DisplayStatType1(1)
#dis.DisplayStatTypeImg(1)
#re.recommandation(2)
re.recommandation(1)

#user.create(3)
#user.createUsers()
#lastElement = img.pop(0)

#user.add_preference(1,25)
#user.remove_preference(1,3)



# classe DAOdeCSV, collect, nettoyage,traitement(classification), display, main
#bdd/JSON => user (id), images(info csv), pref(user/images)

#DAO de JSON(bdd) : 
# - user -> read create
# - images -> read update delete (create si collecte via API)
# - pref -> crud

#collect : co API

#nettoyage : suppr data not use + mis en forme
# - supression des photos avec que 1 type

#traitement : 
# - like photo -> utilisation crud pref
# - ajout tag -> crud image
#- generation des stats pour les courbes

#display
#- generation et affcihage des courbes
#- generation menu

#main
# - appelle display (menu)
# 