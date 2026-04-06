from app.models.user import User
from app.db.session import engine
from app.db.base import Base
from fastapi import FastAPI
from app.routers.auth import router as auth_router
from app.routers.users import router as users_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(users_router)