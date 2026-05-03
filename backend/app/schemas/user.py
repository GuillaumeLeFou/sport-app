from pydantic import BaseModel, EmailStr, ConfigDict, Field
from datetime import date

class UserCreate(BaseModel):
    email: EmailStr = Field(..., example="[EMAIL_ADDRESS]")
    password: str = Field(..., min_length=6, max_length=72, example="password")
    username: str = Field(..., example="username")
    first_name: str = Field(..., example="John")
    last_name: str = Field(..., example="Doe")
    age: int = Field(..., example=25)
    birthday: date = Field(..., example="2000-01-01")
    weight: float = Field(..., example=70.0)
    height: float = Field(..., example=175)

class UserLogin(BaseModel):
    email: EmailStr = Field(..., example="[EMAIL_ADDRESS]")
    password: str = Field(..., min_length=6, max_length=72, example="password")

class UserResponse(BaseModel):
    id: int = Field(..., example=1)
    email: EmailStr = Field(..., example="[EMAIL_ADDRESS]")
    username: str = Field(..., example="username")
    first_name: str = Field(..., example="John")
    last_name: str = Field(..., example="Doe")
    age: int = Field(..., example=25)
    birthday: date = Field(..., example="2000-01-01")
    weight: float = Field(..., example=70.0)
    height: float = Field(..., example=175)

    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str