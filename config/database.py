from dotenv import load_dotenv
load_dotenv()
import os
from pymongo import MongoClient

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)

db = client.student_db
collection_name = db["student_collection"]