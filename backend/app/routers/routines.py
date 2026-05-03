from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.routine import RoutineCreate, RoutineResponse
from app.services.routine_service import create_routine, get_user_routines, update_routine, delete_routine
from app.core.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/routines", tags=["routines"])

@router.post("/", response_model=RoutineResponse, summary="Create a new routine", description="Creates a new routine for the authenticated user.")
def create(
    routine: RoutineCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return create_routine(db, user.id, routine)

@router.get("/", response_model=list[RoutineResponse], summary="Get all routines", description="Returns all routines for the authenticated user.")
def get_all(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return get_user_routines(db, user.id)

@router.put("/{id}", response_model=RoutineResponse, summary="Update a routine", description="Updates a routine for the authenticated user.")
def update(
    id: int,
    routine: RoutineCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return update_routine(db, user.id, id, routine)

@router.delete("/{id}", response_model=RoutineResponse, summary="Delete a routine", description="Deletes a routine for the authenticated user.")
def delete(
    id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return delete_routine(db, user.id, id)
