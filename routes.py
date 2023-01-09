from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
from models import User, UserUpdate
from data_validation import is_email_available, is_email_valid, is_birthday_valid, is_username_available, is_username_valid
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
    is_username_valid(user['username'])
    is_username_available(request, user['username'])
    is_email_available(request, user['email'])

    new_user = request.app.database["users"].insert_one(user)
    created_user = request.app.database["users"].find_one(
        {"_id": new_user.inserted_id}
    )

    return created_user

@router.put("/{id}", response_description="Update a user", response_model=User)
def update_user(id: str, request: Request, user: UserUpdate = Body(...)):
    if request.app.database["users"].find_one({"_id": id}) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {id} not found")
    
    user = user.dict()
    
    #data validation
    if user['username']:
        is_username_valid(user['username'])
        is_username_available(request, user['username'])
    if user['email']:  
        is_email_valid(user['email'])
        is_email_available(request, user['email'])
    if user['birthday']:
        is_birthday_valid(user['birthday'])

    user = {k: v for k, v in user.items() if v is not None} #remove empty keypairs
    if len(user) >= 1:
        update_result = request.app.database["users"].update_one(
            {"_id": id}, {"$set": user}
        )

    existing_book = request.app.database["users"].find_one({"_id": id})
    
    return existing_book

