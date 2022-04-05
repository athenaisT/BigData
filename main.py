from src import display as dis
from src import nettoyage as net
from DAO import DAOuser as user 

# git push https://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@github.com/athenaisT/BigData.git

dis.menu()
#net.transform()
#user.create(3)






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