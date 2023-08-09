from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    username: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    
# class User(BaseModel):
#     username: str
#     email: str
#     password: str 

class Login(BaseModel):
    username: str
    password: str