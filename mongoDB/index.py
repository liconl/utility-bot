import pymongo 
from pymongo import MongoClient
import os

#  You can open and see the data from mongo compass with this string
MONGO_CONNECTION_URL=os.getenv("LUIS_PHONE_NUMBER")

cluster =MongoClient(MONGO_CONNECTION_URL)

# cluster is a collection of "collections"
# collection is a collection of "documents"
# documents is a dict/json object


# clusters
db_twilio =cluster["twilio"]
db_images =cluster["images"]

#collections
funds = db_twilio["funds"]
testImages = db_images["testImages"]
images = db_images["images"]

 
 
