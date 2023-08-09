from typing import Optional
from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    username: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    bio: Optional[str]

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        
        json_schema_extra = {
            "example": {
                "username": "Jane Doe",
                "email": "jdoe@example.com",
                "password": "supersecret"
            } 
        }
# class User(BaseModel):
#     username: str
#     email: str
#     password: str 

class Login(BaseModel):
    username: str
    password: str