"""Configuration for the energy planner.

Every value that can be adjusted without touching the rest of the code lives here.
"""

from pathlib import Path

# --- Where the data is stored ----------------------------------------------
# The data/ folder is listed in .gitignore so personal data never reaches GitHub.
DATA_FOLDER = Path(__file__).parent / "data"
SHIFTS_FILE = DATA_FOLDER / "shifts.csv"
ACTIVITIES_FILE = DATA_FOLDER / "activities.csv"

SHIFT_COLUMNS = ["date", "type", "start_time", "end_time", "energy"]
ACTIVITY_COLUMNS = ["date", "study_min", "cooking_min", "exercise_min"]

# --- My job ----------------------------------------------------------------
SHIFT_TYPES = ["delivery", "sorting"]

# --- My routine (CHANGE THESE VALUES TO YOUR OWN) --------------------------
BEDTIME = "22:30"
REST_MINUTES = 60         # shower, eat and rest after getting home from a shift
DEFAULT_ENERGY = 3        # used when there is no history yet

# --- Energy levels (scale of 1 to 5) ---------------------------------------
LOW_ENERGY_MAX = 2        # 1 and 2 count as low energy
HIGH_ENERGY_MIN = 4       # 4 and 5 count as high energy

# --- Plans for each energy level (CHANGE THESE VALUES TO YOUR OWN) ---------
PLANS = {
    "low": {
        "study_min": 25,
        "cooking_min": 15,
        "exercise_min": 10,
        "study_idea": "Light review of lecture notes",
        "cooking_idea": "Something quick: eggs, leftover rice, stir-fried vegetables",
        "exercise_idea": "Back and leg stretches",
    },
    "medium": {
        "study_min": 50,
        "cooking_min": 30,
        "exercise_min": 20,
        "study_idea": "One focused study block on a single unit",
        "cooking_idea": "A full recipe for today and tomorrow",
        "exercise_idea": "Brisk walk or a short home workout",
    },
    "high": {
        "study_min": 90,
        "cooking_min": 60,
        "exercise_min": 40,
        "study_idea": "Make progress on the hardest assignment of the week",
        "cooking_idea": "Batch cooking for several days",
        "exercise_idea": "Full workout",
    },
}

# --- Weekly goals in minutes (CHANGE THESE VALUES TO YOUR OWN) -------------
WEEKLY_GOALS = {
    "study_min": 300,
    "cooking_min": 150,
    "exercise_min": 120,
}
