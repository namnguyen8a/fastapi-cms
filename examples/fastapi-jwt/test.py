import jwt
from passlib.context import CryptContext
from pydantic import BaseModel

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"


db = {
    "string": {
        "username": "string",
        "password": "string",
    },
}

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hashed_password(password):
    return pwd_context.hash(password)

db["string"]["password"] = hashed_password(db["string"]["password"])

print(type(db["string"]["password"]))
print(db)


def login(username, password):
    if username not in db:
        return {"msg": "incorrect username or password"}
    if not pwd_context.verify(password, db["string"]["password"]):
        return {"msg": "incorrect username or password"}

    return {"msg": "login"}

print(login("string", "string"))
