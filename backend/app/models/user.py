from sqlalchemy import Column, Integer, String, DateTime, Float
from app.db.base import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(Integer)
    weight = Column(Float)
    height = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
