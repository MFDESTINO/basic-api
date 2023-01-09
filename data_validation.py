from fastapi import HTTPException, status
import re
from datetime import datetime

def is_birthday_valid(birthday):
    try:
        datetime.strptime(birthday, '%Y-%m-%d')
    except ValueError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Invalid birthday, should be YYYY-MM-DD")

def is_email_valid(email):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not re.fullmatch(email_regex, email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Invalid email address.")

def is_username_available(request, username):
    if request.app.database["users"].find_one({"username": username}):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Username {username} already exists!")

def is_email_available(request, email):
    if request.app.database["users"].find_one({"email": email}):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"User with email {email} already exists!")