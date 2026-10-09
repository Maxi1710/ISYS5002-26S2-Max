"""Configuration for the energy planner.

Every value that can be adjusted without touching the rest of the code lives here.
"""

from pathlib import Path

# --- Where the data is stored ----------------------------------------------
DATA_FOLDER = Path(__file__).parent / "data"
SHIFTS_FILE = DATA_FOLDER / "shifts.csv"
ACTIVITIES_FILE = DATA_FOLDER / "activities.csv"

# energy = how I feel at the end of the shift, from 1 (exhausted) to 5 (full of energy)
SHIFT_COLUMNS = ["date", "type", "start_time", "end_time", "energy"]
ACTIVITY_COLUMNS = ["date", "study_min", "cooking_min", "exercise_min"]

# --- My job ----------------------------------------------------------------
SHIFT_TYPES = ["delivery", "sorting"]

# --- My routine --------------------------
BEDTIME = "22:00"
REST_MINUTES = 40         # time I need to rest after a shift before starting anything
DEFAULT_ENERGY = 3        # used when there is no history yet
HOURS_MARGIN = 1          # shifts within 1 hour of today's length count as similar

# --- Energy levels (scale of 1 to 5) ---------------------------------------
LOW_ENERGY_MAX = 2        # 1 and 2 count as low energy
HIGH_ENERGY_MIN = 4       # 4 and 5 count as high energy

PLANS = {
    "low": {
        "study_min": 30,
        "cooking_min": 20,
        "exercise_min": 30,
        "study_idea": "Light review of lecture notes",
        "cooking_idea": "Something quick: fried chicken or beef with rice and avocado",
        "exercise_idea": "Back and leg stretches",
    },
    "medium": {
        "study_min": 50,
        "cooking_min": 60,
        "exercise_min": 60,
        "study_idea": "One focused study block on a single unit",
        "cooking_idea": "A full recipe for today and tomorrow",
        "exercise_idea": "Brisk walk or a short home workout",
    },
    "high": {
        "study_min": 90,
        "cooking_min": 90,
        "exercise_min": 120,
        "study_idea": "Make progress on the hardest assignment of the week",
        "cooking_idea": "Batch cooking for several days",
        "exercise_idea": "Full workout",
    },
}

WEEKLY_GOALS = {
    "study_min": 360,
    "cooking_min": 240,
    "exercise_min": 480,
}
