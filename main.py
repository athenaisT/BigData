from src import display as dis
from src import nettoyage as net

dis.print_menu()
net.transform()


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