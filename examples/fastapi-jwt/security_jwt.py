# https://chatgpt.com/c/6841882b-e288-800b-ad2a-5d36d60dd062 (explain jwt flow)

from typing import Annotated
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer

db = {}

class User(BaseModel):
    username: str
    password: str

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/create-user/")
async def create_user(user: User):
    db[user.username] = user.dict()
    return {"msg": "created success!"}

@app.post("/token")
async def login(user: Annotated[User, Depends(oauth2_scheme)]):
    username = user.username
    password = user.password
    if user.username not in db:
        return {"msg": "incorrect username or password"}
    if user.password != db[username]["password"]:
        return {"msg": "incorrect username or password"}
    return {"msg": "login succesful"}

@app.get("/get-users")
async def get_user():
    return db