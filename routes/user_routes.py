from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from models.Users import User, Login
from serializers.user_serializer import single_user_serializer, many_users_serializer
from config.db_config import users_collection
from helpers.status_codes import STATUS_CODE_201, STATUS_CODE_MISSING_FIELDS_400, STATUS_CODE_404, STATUS_CODE_500
from helpers.Hashing import get_password_hash, verify_password


user_router = APIRouter(prefix="/api/auth/users", tags=["Users"])

@user_router.post("/create", status_code=201)
async def create_user(user: User = Body(...)):
    if not user.username or not user.email or not user.password:
        return STATUS_CODE_MISSING_FIELDS_400
    
    try:
        isExisting_doc = await users_collection.find_one({"email": user.email})

        if isExisting_doc:
                return JSONResponse(content={"message": "User already exists"}, status_code=400)

        hashed_pwd = get_password_hash(user.password)

        created_user = {
                    "username": user.username,
                    "email": user.email,
                    "password": hashed_pwd
                }

        new = await users_collection.insert_one(created_user)
        new_user_id = new.inserted_id

        newUser = await users_collection.find_one({"_id": new_user_id})

        res = await single_user_serializer(newUser)
        return STATUS_CODE_201(res)
    except Exception as e:
        print("Exception:", e)
        return STATUS_CODE_500


@user_router.post("/login", status_code=200)
async def login(login: Login):
    if not login.username or not login.password:
        return STATUS_CODE_MISSING_FIELDS_400
    
    user = await users_collection.find_one({"username": login.username})

    # print(user)

    if not user:
        return STATUS_CODE_404
    
    verify_user = verify_password(login.password, user["password"])

    if verify_user:
        return {"message" : "Successfully logged in"}
    else: 
        return JSONResponse(content={"message": "Invalid credentials"}, status_code=401)

    


@user_router.get("/") # Instead of using the serializer, you can use the "response_model" field
async def get_all():
    users =  many_users_serializer(users_collection.find())

    return {"data" : users}