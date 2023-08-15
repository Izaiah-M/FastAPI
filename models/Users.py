from typing import Optional
from pydantic import BaseModel, Field, EmailStr

# Field(...) means that it is required


class User(BaseModel):
    username: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    bio: Optional[str]
    phone: str = Field(...)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True

        json_schema_extra = {
            "example": {
                "username": "Jane Doe",
                "email": "jdoe@example.com",
                "password": "supersecret",
                "phone": "0722306453",
                "bio": "bio",
            }
        }


# class User(BaseModel):
#     username: str
#     email: str
#     password: str


class Login(BaseModel):
    username: str
    password: str
