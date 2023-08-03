from pymongo.mongo_client import MongoClient
import os
import dotenv



dotenv.load_dotenv(dotenv.find_dotenv())

password = os.getenv("PASSWORD_MONGODB")

uri = f"mongodb+srv://anuar200572:{password}@cluster0.plqvoke.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
db = client["RoadMaps"]
user_collection = db["users"]

# cursor = user_collection.find({})
# a = []
# for document in cursor:
#     a.append(document['email'])
# print(len(a))
# print(a)

