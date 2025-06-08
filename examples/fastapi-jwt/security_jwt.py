# https://chatgpt.com/c/6841882b-e288-800b-ad2a-5d36d60dd062 (explain jwt flow)

from typing import Annotated
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer
import jwt

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"


# Database
db = {}

# functions
def hashed_password(password):
    return "hashed" + password

def create_access_token(data):
    data_encode = data.copy()
    encode_jwt = jwt.encode(data_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt

class User(BaseModel):
    username: str
    password: str

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/create-user/")
async def create_user(user: User):
    db[user.username] = user.dict()
    db[user.username]["password"] = hashed_password(db[user.username]["password"])
    return {"msg": "created success!"}

@app.post("/token")
async def login(user: User):
    username = user.username
    password = user.password
    if username not in db:
        return {"msg": "incorrect username or password"}
    if password != db[username]["password"]:
        return {"msg": "incorrect username or password"}
    jwt_token = create_access_token({"sub": username})

    return {"jwt_token": jwt_token}

@app.get("/get-users")
async def get_user():
    return db