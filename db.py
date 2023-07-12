from pymongo.mongo_client import MongoClient
import os
import dotenv



dotenv.load_dotenv(dotenv.find_dotenv())

password = os.getenv("PASSWORD_MONGODB")

uri = f"mongodb+srv://anuar200572:{password}@cluster0.plqvoke.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


