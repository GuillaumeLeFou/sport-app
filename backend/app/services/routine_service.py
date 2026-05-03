from sqlalchemy.orm import Session
from app.models.routine import Routine
from app.schemas.routine import RoutineCreate
from datetime import datetime

def create_routine(db: Session, user_id: int, data: RoutineCreate):
    routine = Routine(
        name=data.name,
        description=data.description,
        user_id=user_id,
        created_at=datetime.utcnow()
    )

    db.add(routine)
    db.commit()
    db.refresh(routine)

    return routine

def get_user_routines(db: Session, user_id: int):
    return db.query(Routine).filter(Routine.user_id == user_id).all()

def update_routine(db: Session, user_id: int, routine_id: int, data: RoutineCreate):
    routine = db.query(Routine).filter(Routine.id == routine_id).first()

    if not routine:
        raise HTTPException(status_code=404, detail="Routine not found")

    routine.name = data.name
    routine.description = data.description

    db.commit()
    db.refresh(routine)

    return routine

def delete_routine(db: Session, user_id: int, routine_id: int):
    routine = db.query(Routine).filter(Routine.id == routine_id).first()

    if not routine:
        raise HTTPException(status_code=404, detail="Routine not found")

    db.delete(routine)
    db.commit()

    return routine
