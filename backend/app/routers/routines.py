from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.routine import RoutineCreate, RoutineResponse
from app.services.routine_service import create_routine, get_user_routines
from app.core.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/routines", tags=["routines"])

@router.post("/", response_model=RoutineResponse)
def create(
    routine: RoutineCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return create_routine(db, user.id, routine)

@router.get("/", response_model=list[RoutineResponse])
def get_all(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return get_user_routines(db, user.id)