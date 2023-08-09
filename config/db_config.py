from motor.motor_asyncio import AsyncIOMotorClient

try:
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    db = client.Trial
    users_collection = db["Users"]

    print("Successfully connected to MongoDB")

except Exception as err:
    print(f"Error connecting to MongoDB - {err}")