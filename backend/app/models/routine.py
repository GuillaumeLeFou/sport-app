from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime
from app.models.relations import routine_exercises

class Routine(Base):
    __tablename__ = "routines"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="routines")
    exercises = relationship(
        "Exercise",
        secondary=routine_exercises,
        back_populates="routines"
    )