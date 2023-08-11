from motor.motor_asyncio import AsyncIOMotorClient
import os

try:
    client = AsyncIOMotorClient(os.environ.get("DB_URL"))
    db = client.Trial
    users_collection = db["Users"]

    print("Successfully connected to MongoDB")

except Exception as err:
    print(f"Error connecting to MongoDB - {err}")