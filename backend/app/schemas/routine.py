from pydantic import BaseModel

class RoutineCreate(BaseModel):
    name: str
    description: str | None = None

class RoutineResponse(BaseModel):
    id: int
    name: str
    description: str | None = None

    class Config:
        from_attributes = True