from sqlalchemy import Table, Column, Integer, ForeignKey
from app.db.base import Base

routine_exercises = Table(
    "routine_exercises",
    Base.metadata,
    Column("routine_id", Integer, ForeignKey("routines.id")),
    Column("exercise_id", Integer, ForeignKey("exercises.id"))
)