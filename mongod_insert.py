#Dependencies

import pandas as pd 
from config import gkey, okey 
import requests
import json 
import pymongo 
import time 
from pprint import pprint

#Method 1#
##########

#Connect to mongo db and create "locations_mdb" database
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

#Create "locations_mdb" database and assign it to a variable
#(note: MongoDB automatically creates a database when you call it, so this can be skipped if you prefer)
db = client.locations_mdb

#Creating or swithcing to a collection
clients = db["clients"]  
hotels = db["hotels"]

#Read and Parse a JSON File
myfile=open("resources/generated.json","r")
json_file=json.load(myfile)

#Load into MongoDB
db.clients.insert_many(json_file)

#Method 2#
##########


# Create a system for specifying api lookup parameters
zips_df=pd.read_csv('resources/zip_codes.csv')
zips_df.head()

#Perform a series of API calls with these parameters
api_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

for index, row in zips_df.iterrows():
    #time.sleep(0.2) (optional, if timeout)
    target_coordinates = f"{zips_df.loc[index, 'Latitude']},{zips_df.loc[index, 'Longitude']}" 
    target_radius = 50000
    target_type = "lodging"
    params = {
        "location": target_coordinates,
        "radius": target_radius,
        "type": target_type,
        "key": gkey}

#--> Request a JSON using our parameters dictionary
    response = requests.get(api_url, params=params).json()
    
#-->Insert the record into MongoDB
    db.hotels.insert_one(response) 
    
#Retrieving Data#
#################

#Retrieve entire collection
records=db.clients.find()
for entry in records:
    pprint(entry)

#Retrieve entries by index and field value:
female_clients=db.clients.find({},{ "gender": "female"})
for entry in female_clients:
    print(entry)

#Retrieve entries by any field and by a range of values:
clients=db.clients.find()
for person in clients:
    balance=person["balance"]
    balance=balance.replace("$","")
    balance=balance.replace(",","")
    balance=float(balance)
    if balance > 2000:
        name=person["name"]
        age=person["age"]
        print(f"Name:{name}, Age:{age}")