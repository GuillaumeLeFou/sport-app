from app.schemas.user import UserCreate, UserResponse, Token
from app.services.auth_service import create_user
from app.db.session import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app.services.auth_service import authenticate_user
from app.core.security import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth",  tags=["auth"])

@router.post("/register", response_model=UserResponse, summary="Register a new user", description="Creates a new user.")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.post("/login", response_model=Token, summary="Login", description="Logs in a user and returns an access token.")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    authenticated_user = authenticate_user(db, form_data.username, form_data.password)

    if not authenticated_user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    access_token = create_access_token(data={"sub": authenticated_user.email})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }