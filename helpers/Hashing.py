import os
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

# to get a secret Key run:
# openssl rand -hex 32

SECRET_KEY = os.environ.get("KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10

pwd_context = CryptContext(schemes=["bcrypt"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Function to verify the password
def verify_password(plain_pwd, hashed_pwd):
    return pwd_context.verify(plain_pwd, hashed_pwd)

# Function to hash the pwd
def get_password_hash(pwd):
    return pwd_context.hash(pwd)
