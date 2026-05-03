from pydantic import BaseModel, Field

class RoutineCreate(BaseModel):
    name: str = Field(..., example="Routine Name")
    description: str | None = Field(None, example="Chest / Shoulders / Triceps")

class RoutineResponse(BaseModel):
    id: int = Field(..., example=1)
    name: str = Field(..., example="Routine Name")
    description: str | None = Field(None, example="Chest / Shoulders / Triceps")

    class Config:
        from_attributes = True