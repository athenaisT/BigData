# génération des 100 user
from DAO import DAOuser as user

def generationUser(num) :
    user.create(num)

def generationCentUsers() :
    for i in range(0,99) :
        generationUser(i)
