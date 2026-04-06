from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.db.session import get_db
from jose import jwt, JWTError
from app.core.config import SECRET_KEY, ALGORITHM
from app.services.auth_service import get_user_by_email

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):   
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        exp = payload.get("exp")
        
        email = payload.get("sub")
        if not email:
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail = "Invalid token",
                headers = {"WWW-Authenticate": "Bearer"},
            )
        
        user = get_user_by_email(db, email)
        if not user:
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail = "User not found",
                headers = {"WWW-Authenticate": "Bearer"},
            )
        
        return user
    except JWTError:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Invalid token",
            headers = {"WWW-Authenticate": "Bearer"},
        )