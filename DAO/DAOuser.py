import json

#read create

def create(numUser):
    jsonFilePath = r"Data/user.json"
    prenom = "jojo"
        
    # create a dictionary
    new = numUser
    data = None
    
    # 1. Read file contents
    with open(jsonFilePath, "r") as read_file:
        data = json.load(read_file)

    # 2. Update json object
    for i in range (100):
        row = {}
        row['Name'] = prenom
        row['Num'] = i

        data[i+1] = row

    #     # 3. Write json file 
  
    with open(jsonFilePath, "w") as file:
       
       json.dump(data, file)
    
    print("user test",data)




