
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from .config import get_settings
from functools import lru_cache
settings=get_settings()

uri = "mongodb+srv://root:{}@cluster0.bew5qxb.mongodb.net/?retryWrites=true&w=majority".format(settings["DB_PASSWORD"])

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db=client["HPMP"]
songs=db["songs"]
users=db["users"]
playlists=db["playlist"]


def check():
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)


def shutdown():
    client.close()