from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.dependencies import get_current_user
from app.models.user import User
from app.services.routine_exercise_service import create_routine_exercise, get_user_routine_exercises, get_routine_exercise, update_routine_exercise, delete_routine_exercise, get_routine_exercises_by_routine_id
from app.schemas.routine_exercise import RoutineExerciseCreate, RoutineExerciseResponse

router = APIRouter(prefix="/routine_exercise", tags=["routine_exercise"])

@router.post("/", response_model=RoutineExerciseResponse, summary="Create a new routine exercise", description="Creates a new routine exercise for the authenticated user.")
def create(
    routine_exercise: RoutineExerciseCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return create_routine_exercise(db, routine_exercise)

@router.get("/", response_model=list[RoutineExerciseResponse], summary="Get all routine exercises", description="Returns all routine exercises for the authenticated user.")
def get_all(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return get_user_routine_exercises(db, user.id)

@router.get("/{id}", response_model=RoutineExerciseResponse, summary="Get a routine exercise", description="Returns a routine exercise for the authenticated user.")
def get_one(
    id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return get_routine_exercise(db, user.id, id)

@router.get("/routine/{routine_id}/", response_model=list[RoutineExerciseResponse], summary="Get all routine exercises by routine id", description="Returns all routine exercises for the authenticated user by routine id.")
def get_all_by_routine_id(
    routine_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return get_routine_exercises_by_routine_id(db, user.id, routine_id)

@router.put("/{id}", response_model=RoutineExerciseResponse, summary="Update a routine exercise", description="Updates a routine exercise for the authenticated user.")
def update(
    id: int,
    routine_exercise: RoutineExerciseCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return update_routine_exercise(db, user.id, id, routine_exercise)

@router.delete("/{id}", response_model=RoutineExerciseResponse, summary="Delete a routine exercise", description="Deletes a routine exercise for the authenticated user.")
def delete(
    id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return delete_routine_exercise(db, user.id, id)