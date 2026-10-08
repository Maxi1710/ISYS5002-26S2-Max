"""Recommendations: turns energy and free time into a plan for today."""

import config


def energy_level(energy):
    """Classify the energy (1 to 5) as low, medium or high."""
    if energy <= config.LOW_ENERGY_MAX:
        return "low"
    if energy >= config.HIGH_ENERGY_MIN:
        return "high"
    return "medium"


def create_plan(energy, available_minutes):
    """Create the plan for the day.

    Starts from the base plan of the energy level. If the plan does not fit
    in the available time, the three activities are reduced by the same proportion.
    """
    level = energy_level(energy)
    base = config.PLANS[level]

    plan_minutes = base["study_min"] + base["cooking_min"] + base["exercise_min"]
    factor = 1
    if plan_minutes > available_minutes:
        factor = available_minutes / plan_minutes

    plan = {
        "level": level,
        "study_min": int(base["study_min"] * factor),
        "cooking_min": int(base["cooking_min"] * factor),
        "exercise_min": int(base["exercise_min"] * factor),
        "study_idea": base["study_idea"],
        "cooking_idea": base["cooking_idea"],
        "exercise_idea": base["exercise_idea"],
        "was_reduced": factor < 1,
    }
    return plan
