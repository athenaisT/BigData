import os

menu_options = {
    1: 'Images',
    2: 'Stats user',
    4: 'Exit',
}

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1():
    clearConsole()
    print('Images\'Option 1\'')
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

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Mauvais numéro ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 4:
            print('Au revoir')
            exit()
        else:
            print('Mauvaise saisie.')
