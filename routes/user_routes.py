from fastapi import APIRouter
from models.Users import User
from serializers.user_serializer import single_user_serializer, many_users_serializer
from config.db_config import users_collection
from helpers.status_codes import STATUS_CODE_201, STATUS_CODE_MISSING_FIELDS_400
from helpers.Hashing import get_password_hash, verify_password


user_router = APIRouter(prefix="/api/auth/users")

@user_router.post("/create", status_code=201)
async def create_user(user: User):
    if not user.username or not user.email or not user.password:
        return STATUS_CODE_MISSING_FIELDS_400
    
    hashed_pwd = get_password_hash(user.password)

    created_user = {
        "username": user.username,
        "email": user.email,
        "password": hashed_pwd
    }


    new = users_collection.insert_one(created_user)
    new_user_id = new.inserted_id

    newUser = single_user_serializer(users_collection.find_one({"_id": new_user_id}))

    return STATUS_CODE_201(newUser)


@user_router.get("/") # Instead of using the serializer, you can use the "response_model" field
async def get_all():
    users =  many_users_serializer(users_collection.find())

    return {"data" : users}