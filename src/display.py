#import matplotlib.pyplot as plt
import os
from src import user as user
from src import image as image
import matplotlib.pyplot as plt


#display
#- generation et affcihage des courbes
#- generation menu


#trace courbe/cambert etc des préférence de l'user sur la couleur
def DisplayStatCouleur():
    user.getImg_pref(1)
    print()

    


#trace courbe/cambert etc des préférence de l'user sur le type1
def DisplayStatType1(iduser):
    id_img=user.getImg_pref(iduser)
    types=[]
    distinctType = []
    for id in id_img:
        type1 = image.recup_type1(id)
        if type1 not in distinctType :
                distinctType.append(type1)
        types.append(type1)
    
    typeNumber = []
    for i in range (len(distinctType)):
        typeNumber.append(types.count(distinctType[i]))

    c = ['red', 'yellow', 'green', 'blue', 'purple']
    plt.bar(distinctType,typeNumber ,color=c)
    plt.title('Diagramme de preference du type 1', fontsize=10)
    plt.savefig("type1.png")
    plt.show()


#trace courbe/cambert etc des préférence de l'user sur le type2
def DisplayStatType2(iduser):
    id_img=user.getImg_pref(iduser)
    types=[]
    distinctType = []
    for id in id_img:
        type2 = image.recup_type2(id)
        if type2 not in distinctType :
                distinctType.append(type2)
        types.append(type2)
    
    typeNumber = []
    for i in range (len(distinctType)):
        typeNumber.append(types.count(distinctType[i]))

    c = ['red', 'yellow', 'green', 'blue', 'purple']
    plt.bar(distinctType,typeNumber ,color=c)
    plt.title('Diagramme de preference du type 2', fontsize=10)
    plt.savefig("type2.png")
    plt.show()

#trace courbe/cambert etc des préférence de l'user sur le type image
def DisplayStatTypeImg(iduser):
    id_img=user.getImg_pref(iduser)
    types=[0,0]
    for id in id_img:
        if image.recup_typeImg(id)==True:
            #c'est png
            types[0]+=1
        else:
            #c'est jpg
            types[1]+=1

    #print("yeyt",types)
    plt.pie(types,labels=["png","jpg"],colors=["red","green"], normalize=True)
    plt.show()


def DisplayStatTag(iduser):
    id_img=user.getImg_pref(iduser)
    types=[]
    distinctTags = []
    for id in id_img:
        Tags = image.recup_tag(id)
        for tag in  Tags :
            if tag not in distinctTags :
                distinctTags.append(tag)
            types.append(tag)

    tagNumber = []
    for i in range (len(distinctTags)):
        tagNumber.append(types.count(distinctTags[i]))

    c = ['red', 'yellow', 'green', 'blue', 'purple']
    plt.bar(distinctTags,tagNumber ,color=c)
    plt.title('Diagramme de preference de tag', fontsize=10)
    plt.savefig("tag.png")
    plt.show()

 
# #data
# x = [1, 2, 3, 4, 5]
# h = [10, 8, 12, 4, 7]
# c = ['red', 'yellow', 'black', 'blue', 'orange']
 
# #bar plot
# plt.bar(x, height = h, color = c)
 
# plt.show()

################################Affichage Menue

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def print_menu():
    menu_options = {
    1: 'Statistiques',
    2: 'Stats user',
    4: 'Exit',
    }
    #1 - start - generation user
    #2 - stats type 1 ----> choisir numéro user
    #3 - stat type 2 ----> choisir numéro user
    #4 - stat type Img ----> choisir numéro user
    #5 - stat couleur ----> choisir numéro user
    #6 - recommandation (que lui montrer ?)
    #7 - exit

    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def statistique():
    clearConsole()
    #print("mange tes morts")
    #print('Images\'Option 1\'')
    try:
        option = int(input('Enter your choice: '))
    except:
        print('Mauvais numéro ...')


def option2():
     clearConsole()
     print('Stat\'Option 2\'')
     try:
        option = int(input('Enter your choice: '))
     except:
        print('Mauvais numéro ...')

def menu():
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Mauvais numéro ...')
        #Check what choice was entered and act accordingly
        if option == 1:
            statistique()
        elif option == 2:
            option2()
        elif option == 4:
            print('Au revoir')
            exit()
        else:
            print('Mauvaise saisie.')