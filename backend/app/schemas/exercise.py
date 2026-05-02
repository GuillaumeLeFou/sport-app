from pydantic import BaseModel

class ExerciseCreate(BaseModel):
    name: str
    description: str | None = None
    instructions: str | None = None
    muscle_group: str | None = None
    exercise_type: str | None = None
    equipment_needed: str | None = None
    global_exercise: bool = False

class ExerciseResponse(BaseModel):
    id: int
    name: str
    description: str | None = None
    instructions: str | None = None
    muscle_group: str | None = None
    exercise_type: str | None = None
    equipment_needed: str | None = None
    global_exercise: bool = False

    class Config:
        from_attributes = True