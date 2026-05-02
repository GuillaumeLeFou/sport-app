from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.exercise import ExerciseCreate, ExerciseResponse
from app.services.exercise_service import create_exercise, get_user_exercises, get_exercise
from app.core.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/exercises", tags=["exercises"])

@router.post("/", response_model=ExerciseResponse)
def create(
    exercise: ExerciseCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return create_exercise(db, user.id, exercise)

@router.get("/", response_model=list[ExerciseResponse])
def get_all(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return get_user_exercises(db, user.id)

@router.get("/{id}", response_model=ExerciseResponse)
def get_one(
    id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return get_exercise(db, id)