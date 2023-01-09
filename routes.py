from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
from models import User
from data_validation import is_email_available, is_email_valid, is_birthday_valid, is_username_available
import uuid

router = APIRouter()


@router.get("/", response_description="List all users", response_model=List[User])
def list_users(request: Request):
    users = list(request.app.database["users"].find(limit=100))
    return users

@router.post("/", response_description="Create a new user", status_code=status.HTTP_201_CREATED, response_model=User)
def create_user(request: Request, user: User = Body(...)):
    user = jsonable_encoder(user)
    user['_id'] = str(uuid.uuid4()) #generate unique id

    #data validation
    is_email_valid(user['email'])
    is_birthday_valid(user['birthday'])
    is_username_available(request, user['username'])
    is_email_available(request, user['email'])

    new_user = request.app.database["users"].insert_one(user)
    created_user = request.app.database["users"].find_one(
        {"_id": new_user.inserted_id}
    )

    return created_user

