import app.models
from app.db.session import engine
from app.db.base import Base
from fastapi import FastAPI
from app.routers.auth import router as auth_router
from app.routers.users import router as users_router
from app.routers.routines import router as routines_router
from app.routers.exercises import router as exercises_router
from app.routers.routine_exercise import router as routine_exercise_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(routines_router)
app.include_router(exercises_router)
app.include_router(routine_exercise_router)