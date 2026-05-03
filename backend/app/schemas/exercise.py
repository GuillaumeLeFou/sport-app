from pydantic import BaseModel, Field

class ExerciseCreate(BaseModel):
    name: str = Field(..., example="Chest press")
    description: str | None = Field(None, example="Develop chest strength and size")
    instructions: str | None = Field(None, example="Bench press is a chest exercise that is performed while lying on a bench.")
    muscle_group: str | None = Field(None, example="Chest / Shoulders / Triceps")
    exercise_type: str | None = Field(None, example="Compound")
    equipment_needed: str | None = Field(None, example="Bench / Dumbbells")
    global_exercise: bool = Field(False, example=False)

class ExerciseResponse(BaseModel):
    id: int = Field(..., example=1)
    name: str = Field(..., example="Chest press")
    description: str | None = Field(None, example="Develop chest strength and size")
    instructions: str | None = Field(None, example="Bench press is a chest exercise that is performed while lying on a bench.")
    muscle_group: str | None = Field(None, example="Chest / Shoulders / Triceps")
    exercise_type: str | None = Field(None, example="Compound")
    equipment_needed: str | None = Field(None, example="Bench / Dumbbells")
    global_exercise: bool = Field(False, example=False)

    class Config:
        from_attributes = True