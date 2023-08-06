from fastapi import APIRouter
from models.Users import User
from serializers.user_serializer import single_user_serializer, many_users_serializer
from config.db_config import users_collection
from helpers.status_codes import STATUS_CODE_200


user_router = APIRouter(prefix="/api/users")

@user_router.post("/create")
async def create_user(user: User):
    if not user.username or not user.email or not user.password:
        return {"message": "Missing fields!"}, 400
    
    new = users_collection.insert_one(dict(user))
    new_user_id = new.inserted_id

    newUser = single_user_serializer(users_collection.find_one({"_id": new_user_id}))

    return STATUS_CODE_200(newUser)


@user_router.get("/")
async def get_all():
    users =  many_users_serializer(users_collection.find())

    return {"data" : users}