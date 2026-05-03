from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.exercise import Exercise
from app.schemas.exercise import ExerciseCreate
from datetime import datetime

def create_exercise(db: Session, user_id: int, data: ExerciseCreate):

    exercise = Exercise(
        name=data.name,
        description=data.description,
        instructions=data.instructions,
        muscle_groups=data.muscle_groups,
        exercise_type=data.exercise_type,
        equipment_needed=data.equipment_needed,
        global_exercise=data.global_exercise,

        user_id=None if data.global_exercise else user_id,

        created_at=datetime.utcnow()
    )

    db.add(exercise)
    db.commit()
    db.refresh(exercise)

    return exercise

def get_user_exercises(db: Session, user_id: int):

    return db.query(Exercise).filter(
        Exercise.deleted_at == None,
        (
            Exercise.global_exercise == True |
            Exercise.user_id == user_id
        )
    ).all()

def get_exercise(db: Session, id: int):

    return db.query(Exercise).filter(
        Exercise.id == id,
        Exercise.deleted_at == None
    ).first()

def update_exercise(db: Session, user_id: int, exercise_id: int, data: ExerciseCreate):

    exercise = db.query(Exercise).filter(
        Exercise.id == exercise_id,
        Exercise.deleted_at == None,
        Exercise.user_id == user_id 
    ).first()

    if not exercise:
        raise HTTPException(status_code=404, detail="Exercise not found")

    exercise.name = data.name
    exercise.description = data.description
    exercise.instructions = data.instructions
    exercise.muscle_groups = data.muscle_groups
    exercise.exercise_type = data.exercise_type
    exercise.equipment_needed = data.equipment_needed

    db.commit()
    db.refresh(exercise)

    return exercise

def delete_exercise(db: Session, user_id: int, exercise_id: int):

    exercise = db.query(Exercise).filter(
        Exercise.id == exercise_id,
        Exercise.deleted_at == None
    ).first()

    if not exercise:
        raise HTTPException(status_code=404, detail="Exercise not found")

    if exercise.global_exercise:
        raise HTTPException(
            status_code=403,
            detail="Global exercises cannot be deleted"
        )

    if exercise.user_id != user_id:
        raise HTTPException(
            status_code=403,
            detail="Not allowed to delete this exercise"
        )

    exercise.deleted_at = datetime.utcnow()

    db.commit()
    db.refresh(exercise)

    return exercise