from pymongo import MongoClient
import os

def get_mongo_db():
    MONGODB_URI = os.environ.get('MONGODB_URI')
    database_name = os.environ.get('DATABASE_NAME')
    client = MongoClient(MONGODB_URI)
    db = client[database_name]
    print('Database connected successfully.')
    return db
