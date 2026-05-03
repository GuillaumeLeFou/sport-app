from sqlalchemy.orm import Session
from app.models.routine_exercise import RoutineExercise
from app.models.routine import Routine
from app.schemas.routine_exercise import RoutineExerciseCreate
from datetime import datetime

def create_routine_exercise(db: Session, data: RoutineExerciseCreate):
    routine_exercise = RoutineExercise(
        routine_id=data.routine_id,
        exercise_id=data.exercise_id,
        sets=data.sets,
        reps=data.reps,
        weight=data.weight,
        break_time=data.break_time,
        order=data.order,
        created_at=datetime.utcnow()
    )

    db.add(routine_exercise)
    db.commit()
    db.refresh(routine_exercise)

    return routine_exercise

def get_user_routine_exercises(db: Session, user_id: int):
    routine_exercises = db.query(RoutineExercise).join(Routine).filter(Routine.user_id == user_id).all()
    return routine_exercises

def get_routine_exercise(db: Session, user_id: int, id: int):
    return db.query(RoutineExercise).join(Routine).filter(Routine.user_id == user_id, RoutineExercise.id == id).first()

def update_routine_exercise(db: Session, user_id: int, id: int, data: RoutineExerciseCreate):
    routine_exercise = db.query(RoutineExercise).join(Routine).filter(Routine.user_id == user_id, RoutineExercise.id == id).first()

    if not routine_exercise:
        raise HTTPException(status_code=404, detail="Routine exercise not found")

    routine_exercise.routine_id = data.routine_id
    routine_exercise.exercise_id = data.exercise_id
    routine_exercise.sets = data.sets
    routine_exercise.reps = data.reps
    routine_exercise.weight = data.weight
    routine_exercise.break_time = data.break_time
    routine_exercise.order = data.order

    db.commit()
    db.refresh(routine_exercise)

    return routine_exercise

def delete_routine_exercise(db: Session, user_id: int, id: int):
    routine_exercise = db.query(RoutineExercise).join(Routine).filter(Routine.user_id == user_id, RoutineExercise.id == id).first()

    if not routine_exercise:
        raise HTTPException(status_code=404, detail="Routine exercise not found")

    db.delete(routine_exercise)
    db.commit()

    return routine_exercise

def get_routine_exercises_by_routine_id(db: Session, user_id: int, routine_id: int):
    routine = db.query(Routine).filter(Routine.user_id == user_id, Routine.id == routine_id).first()

    if not routine:
        raise HTTPException(status_code=404, detail="Routine not found")
    
    routine_exercises = db.query(RoutineExercise).filter(RoutineExercise.routine_id == routine_id).order_by(RoutineExercise.order).all()
    return routine_exercises