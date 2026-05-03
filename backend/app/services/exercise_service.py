from sqlalchemy.orm import Session
from app.models.exercise import Exercise
from app.schemas.exercise import ExerciseCreate
from datetime import datetime

def create_exercise(db: Session, user_id: int, data: ExerciseCreate):
    exercise = Exercise(
        name=data.name,
        description=data.description,
        instructions=data.instructions,
        muscle_group=data.muscle_group,
        exercise_type=data.exercise_type,
        equipment_needed=data.equipment_needed,
        global_exercise=data.global_exercise,
        user_id=user_id,
        created_at=datetime.utcnow()
    )

    db.add(exercise)
    db.commit()
    db.refresh(exercise)

    return exercise

def get_user_exercises(db: Session, user_id: int):
    global_exercises = db.query(Exercise).filter(Exercise.global_exercise == True).all()
    user_exercises = db.query(Exercise).filter(Exercise.user_id == user_id).all()

    return global_exercises + user_exercises

def get_exercise(db: Session, id: int):
    return db.query(Exercise).filter(Exercise.id == id).first()

def update_exercise(db: Session, user_id: int, exercise_id: int, data: ExerciseCreate):
    exercise = db.query(Exercise).filter(Exercise.id == exercise_id).first()

    if not exercise:
        raise HTTPException(status_code=404, detail="Exercise not found")

    exercise.name = data.name
    exercise.description = data.description
    exercise.instructions = data.instructions
    exercise.muscle_group = data.muscle_group
    exercise.exercise_type = data.exercise_type
    exercise.equipment_needed = data.equipment_needed
    exercise.global_exercise = data.global_exercise

    db.commit()
    db.refresh(exercise)

    return exercise

def delete_exercise(db: Session, user_id: int, exercise_id: int):
    exercise = db.query(Exercise).filter(Exercise.id == exercise_id).first()

    if not exercise:
        raise HTTPException(status_code=404, detail="Exercise not found")

    db.delete(exercise)
    db.commit()

    return exercise

