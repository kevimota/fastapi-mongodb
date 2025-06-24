from pymongo import AsyncMongoClient
from pymongo.server_api import ServerApi
import os

mongo_user = os.environ["MONGO_INITDB_ROOT_USERNAME"]
mongo_pass = os.environ["MONGO_INITDB_ROOT_PASSWORD"]

uri = f"mongodb://{mongo_user}:{mongo_pass}@mongodb:27017"

client = AsyncMongoClient(uri)
dcs_db = client.dcs_db
env_data_col = dcs_db["env_data"]

client = AsyncMongoClient(uri)
dcs_db = client.dcs_db