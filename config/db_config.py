from pymongo import MongoClient

try:
    client = MongoClient("mongodb://localhost:27017")

    print("Successfully connected to MongoDB")


    db = client.Trial

    users_collection = db["Users"]

except Exception as err:
    print(f"Error connecting to MongoDB - {err}")