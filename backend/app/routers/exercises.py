from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.exercise import ExerciseCreate, ExerciseResponse
from app.services.exercise_service import create_exercise, get_user_exercises, get_exercise, update_exercise, delete_exercise
from app.core.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/exercises", tags=["exercises"])

@router.post("/", response_model=ExerciseResponse, summary="Create a new exercise", description="Creates a new exercise for the authenticated user.")
def create(
    exercise: ExerciseCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return create_exercise(db, user.id, exercise)

@router.get("/", response_model=list[ExerciseResponse], summary="Get all exercises", description="Returns all exercises for the authenticated user.")
def get_all(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return get_user_exercises(db, user.id)

@router.get("/{id}", response_model=ExerciseResponse, summary="Get an exercise", description="Returns an exercise for the authenticated user.")
def get_one(
    id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return get_exercise(db, id)

@router.put("/{id}", response_model=ExerciseResponse, summary="Update an exercise", description="Updates an exercise for the authenticated user.")
def update(
    id: int,
    exercise: ExerciseCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return update_exercise(db, user.id, id, exercise)

@router.delete("/{id}", response_model=ExerciseResponse, summary="Delete an exercise", description="Deletes an exercise for the authenticated user.")
def delete(
    id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return delete_exercise(db, user.id, id)

    