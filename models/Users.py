from typing import Optional
from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    username: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    bio: Optional[str]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        
        schema_extra = {
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