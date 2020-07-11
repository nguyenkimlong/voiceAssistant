

import json
import pandas as pd

with open("intents.json", "r+") as file:
    data = json.load(file)
    df = pd.read_excel('data/dialog_talk_agent.xlsx')
    df.head(20)
    df.shape[0]
    df.ffill(axis=0, inplace=True)  # fills the null value with the previous value.
 
    df = pd.DataFrame(df)
    for label, _patterns in df.iterrows():
        data.update(a_dictionary)
        file.seek(0)
        json.dump(data, file)
        data['intents']
    

# def updateJsonFile():
#     jsonFile = open("intents.json", "r") # Open the JSON file for reading
#     data = json.load(jsonFile) # Read the JSON into the buffer
#     jsonFile.close() # Close the JSON file

#     ## Working with buffered content

#     # tmp = data["location"] 
#     # data["location"] = path
#     # data["mode"] = "replay"
#     # read data train
#     df = pd.read_excel('data/dialog_talk_agent.xlsx')
#     df.head(20)
#     df.shape[0]
#     df.ffill(axis=0, inplace=True)  # fills the null value with the previous value.
#     # df
#     df = pd.DataFrame(df)
    
#     for label, _patterns in df.iterrows():

#         data.app


#     ## Save our changes to JSON file
#     jsonFile = open("intents.json", "w+")
#     jsonFile.write(json.dumps(data))
#     jsonFile.close()