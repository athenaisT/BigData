from PIL import Image
import json

#read create

def create(numUser):
    jsonFilePath = r'../Data/user.json'
        
    # create a dictionary
    data = {numUser}
    
    with open('data.txt', 'w') as outfile:  
        json.dump(data, outfile)

    print("user test",data)



create("3")

