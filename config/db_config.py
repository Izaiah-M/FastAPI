from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

# load the env variables
load_dotenv()

# Get the value of the DB_URL variable
url = os.getenv("DB_URL")

try:
    print(url)
    client = AsyncIOMotorClient(url)
    db = client.Trial
    users_collection = db["Users"]
    otp_collection = db["OTP"]

    print("Successfully connected to MongoDB")

except Exception as err:
    print(f"Error connecting to MongoDB - {err}")