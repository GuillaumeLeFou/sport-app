from sqlalchemy import Column, Integer, ForeignKey, DateTime
from app.db.base import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class RoutineExercise(Base):
    __tablename__ = "routine_exercises"

    id = Column(Integer, primary_key=True, index=True)
    routine_id = Column(Integer, ForeignKey("routines.id"))
    exercise_id = Column(Integer, ForeignKey("exercises.id"))
    sets = Column(Integer, nullable=True)
    reps = Column(Integer, nullable=True)
    weight = Column(Integer, nullable=True)
    break_time = Column(Integer, nullable=True)
    order = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    routine = relationship(
        "Routine",
        back_populates="routine_exercises"
    )

    exercise = relationship(
        "Exercise",
        back_populates="routine_exercises"
    )