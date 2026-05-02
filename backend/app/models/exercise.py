from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.models.relations import routine_exercises


class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(Text, nullable=True)

    routines = relationship(
        "Routine",
        secondary=routine_exercises,
        back_populates="exercises"
    )