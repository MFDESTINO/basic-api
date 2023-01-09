import uuid
from typing import Optional
from pydantic import BaseModel, Field

class User(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    username: str = Field(...)
    name: str = Field(...)
    email: str = Field(...)
    birthday: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "username": "MFDOOM",
                "email": "mfdoom@gmail.com",
                "name": "Daniel Dumile",
                "birthday": "1971-7-13"
            }
        }

class UserUpdate(BaseModel):
    username: Optional[str]
    name: Optional[str]
    email: Optional[str]
    birthday: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "username": "MFDOOM",
                "email": "mfdoom@gmail.com",
                "name": "Daniel Dumile",
                "birthday": "1971-7-13"
            }
        }