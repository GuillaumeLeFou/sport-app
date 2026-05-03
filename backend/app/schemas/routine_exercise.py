from pydantic import BaseModel, Field

class RoutineExerciseCreate(BaseModel):
    routine_id: int = Field(..., example=1)
    exercise_id: int = Field(..., example=1)
    sets: int | None = Field(None, example=3)
    reps: int | None = Field(None, example=10)
    weight: int | None = Field(None, example=100)
    break_time: int | None = Field(None, example=60)
    order: int | None = Field(None, example=1)

class RoutineExerciseResponse(BaseModel):
    id: int = Field(..., example=1)
    routine_id: int = Field(..., example=1)
    exercise_id: int = Field(..., example=1)
    sets: int | None = Field(None, example=3)
    reps: int | None = Field(None, example=10)
    weight: int | None = Field(None, example=100)
    break_time: int | None = Field(None, example=60)
    order: int | None = Field(None, example=1)

    class Config:
        from_attributes = True