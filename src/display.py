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
    for id in id_img:
        types.append(image.recup_type1(id))
    
    plt.hist(types)
    plt.title('Test', fontsize=10)
    plt.savefig("type1.png")
    plt.show()


#trace courbe/cambert etc des préférence de l'user sur le type2
def DisplayStatType2(iduser):
    id_img=user.getImg_pref(iduser)
    types=[]
    for id in id_img:
        types.append(image.recup_type2(id))
    
    plt.hist(types)
    plt.title('Test', fontsize=10)
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

    print("yeyt",types)
    plt.pie(types,labels=["png","jpg"],colors=["red","green"], normalize=True)
    plt.show()



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

    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def statistique():
    clearConsole()
    print("mange tes morts")
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