from pymongo import MongoClient
import os
from dotenv import load_dotenv

def get_database():
    dotenv_path = os.path.join(os.path.dirname(__file__), "../.env")

    load_dotenv(dotenv_path)
    mongo_uri = os.getenv("MONGODB_URI")

    if not mongo_uri:
        raise ValueError("mongo_uri environment variable is not set")

    client = MongoClient(mongo_uri)

    db = client["nexgen"]
    return db

def register(user, password):
    db = get_database()
    collection = db["users"]
    
    user = collection.find_one({"email": user})
    if user:
       return "Error: User already exists, use a different email id!" 

    document = {
        "email": user, 
        "password": password
    }
    try:
        collection.insert_one(document)
        return ""
    except errors.DuplicateKeyError:
        return "Error: Duplicate _id detected!"
    except errors.ServerSelectionTimeoutError:
        return "Error: Could not connect to MongoDB Atlas!"
    except errors.OperationFailure:
        return "Error: Authentication failed!"
    except Exception as e:
        return f"Unexpected error: {e}"


def login(user, password):
    db = get_database()
    collection = db["users"]
    
    user_data = collection.find_one({"email": user})
    password_stored = user_data["password"]
    
    if password != password_stored:
        return "Error: Wrong password, please enter the right password"
    
    return ""
    
    
    
    
    
    
    
    