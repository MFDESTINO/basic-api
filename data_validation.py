from fastapi import HTTPException, status
import re
from datetime import datetime

def is_birthday_valid(birthday: str):
    """Check if birthday is a valid date"""

    try:
        datetime.strptime(birthday, '%Y-%m-%d')
    except ValueError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Invalid birthday, should be YYYY-MM-DD")

def is_email_valid(email: str):
    """Check if email is valid."""

    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not re.fullmatch(email_regex, email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Invalid email address.")

def is_username_valid(username: str):
    """
    Check if username is valid:
    - Username must be between 5 and 25 characters
    - Only alphanumeric characters, underscores and dot
    - Underscore and dot cant be at the start or the end
    - Underscore and dot cant be next to each other (__, _., ..)
    """

    username_regex = r'^(?=.{5,25}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$'
    if not re.fullmatch(username_regex, username):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Invalid username.")

def is_username_available(request, username: str):
    """Check if username is available in the database"""

    if request.app.database["users"].find_one({"username": username}):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Username {username} already exists!")

def is_email_available(request, email: str):
    """Check if email is available in the database"""

    if request.app.database["users"].find_one({"email": email}):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"User with email {email} already exists!")