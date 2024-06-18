from fastapi import FastAPI
from uuid import UUID, uuid4
from models import User, Gender, Roles
from typing import List

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("42398675-0ac4-4882-ba64-3a63f015b205"),
        first_name="John",
        last_name="Doe",
        middle_name="Smith",
        gender=Gender.male,
        roles=[Roles.Admin]
    ),
    User(
        id=UUID("42398675-0ac4-4882-ba64-3a63f015b206"),
        first_name="Jeana",
        last_name="Ortega",        
        gender=Gender.female,
        roles=[Roles.Admin, Roles.Dev]
    )
]
#instacia da aplicação
@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/api/v1/users")
async def read_users():
    return db
