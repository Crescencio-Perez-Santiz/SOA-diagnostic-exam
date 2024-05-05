# database_connection.py
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv
import os

load_dotenv()

def get_db_connection():
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')
    client = MongoClient(f"mongodb://{host}:{port}/")
    try:
        client.admin.command('ismaster')
        print("Database connection successful.")
    except ConnectionFailure:
        print("Database connection failed.")
        return None
    return client[db_name]