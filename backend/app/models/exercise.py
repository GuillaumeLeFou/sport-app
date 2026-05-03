from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.models.routine_exercise import RoutineExercise
from datetime import datetime


class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=False, nullable=False)
    description = Column(Text, nullable=True)
    instructions = Column(Text, nullable=True)
    muscle_group = Column(String, nullable=True)
    exercise_type = Column(String, nullable=True)
    equipment_needed = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    global_exercise = Column(Boolean, default=False)

    routine_exercises = relationship("RoutineExercise", back_populates="exercise")