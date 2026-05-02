from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.models.relations import routine_exercises
from datetime import datetime


class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(Text, nullable=True)
    instructions = Column(Text, nullable=True)
    muscle_group = Column(String, nullable=True)
    exercise_type = Column(String, nullable=True)
    equipment_needed = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    global_exercise = Column(Boolean, default=False)

    routines = relationship(
        "Routine",
        secondary=routine_exercises,
        back_populates="exercises"
    )