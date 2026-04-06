from pydantic import BaseModel, EmailStr, ConfigDict, Field
from datetime import date

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=72)
    username: str
    first_name: str
    last_name: str
    age: int
    birthday: date
    weight: float
    height: float

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    username: str
    first_name: str
    last_name: str
    age: int
    birthday: date
    weight: float
    height: float

    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str