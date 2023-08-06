# creating models to create post requests
from typing import Optional
from pydantic import BaseModel


class Role(BaseModel):
    name: str
    desc: str

class Test(BaseModel):
    username: str
    email: Optional[str]
    password: str
    role: Role