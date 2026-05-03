from enum import Enum


class MuscleGroup(str, Enum):
    CHEST = "Chest"
    BACK = "Back"
    SHOULDERS = "Shoulders"
    BICEPS = "Biceps"
    TRICEPS = "Triceps"
    LEGS = "Legs"
    GLUTES = "Glutes"
    CORE = "Core"
    FULL_BODY = "Full Body"


class ExerciseType(str, Enum):
    COMPOUND = "Compound"
    ISOLATION = "Isolation"
    CARDIO = "Cardio"
    MOBILITY = "Mobility"