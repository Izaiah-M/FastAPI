async def single_user_serializer(
    user,
) -> dict:  # Shall return a single user from the db well serialized
    return {"id": str(user["_id"]), "name": user["username"], "email": user["email"]}


async def many_users_serializer(users) -> list:  # shall return a list of users
    return [await single_user_serializer(user) for user in users]
