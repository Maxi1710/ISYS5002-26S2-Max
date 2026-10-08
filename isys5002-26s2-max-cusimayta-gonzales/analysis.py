"""Analysis: calculations on the history of shifts and activities."""

from datetime import date, datetime, timedelta

import config

TIME_FORMAT = "%H:%M"


def duration_in_hours(start_time, end_time):
    """Calculate how many hours a shift lasted."""
    start = datetime.strptime(start_time, TIME_FORMAT)
    end = datetime.strptime(end_time, TIME_FORMAT)
    if end <= start:
        # The shift ended after midnight.
        end = end + timedelta(days=1)
    return (end - start).total_seconds() / 3600


def predict_energy(shifts, shift_type):
    """Predict the energy after a shift using the average of shifts of the same type.

    Returns two values: the estimated energy and how many shifts were used.
    If there is no history for that type, returns the default energy and 0.
    """
    total = 0
    count = 0
    for shift in shifts:
        if shift["type"] == shift_type:
            total = total + shift["energy"]
            count = count + 1
    if count == 0:
        return config.DEFAULT_ENERGY, 0
    return total / count, count


def free_minutes(end_time):
    """Minutes between the end of the shift and bedtime, minus the rest time."""
    end = datetime.strptime(end_time, TIME_FORMAT)
    bedtime = datetime.strptime(config.BEDTIME, TIME_FORMAT)
    if bedtime <= end:
        bedtime = bedtime + timedelta(days=1)
    free = (bedtime - end).total_seconds() / 60 - config.REST_MINUTES
    if free < 0:
        return 0
    return int(free)


def summary_by_type(shifts):
    """For each shift type: count, average hours and average energy."""
    summary = {}
    for shift_type in config.SHIFT_TYPES:
        count = 0
        total_hours = 0
        total_energy = 0
        for shift in shifts:
            if shift["type"] == shift_type:
                count = count + 1
                total_hours = total_hours + duration_in_hours(
                    shift["start_time"], shift["end_time"]
                )
                total_energy = total_energy + shift["energy"]
        if count > 0:
            summary[shift_type] = {
                "count": count,
                "average_hours": total_hours / count,
                "average_energy": total_energy / count,
            }
    return summary


def totals_last_7_days(activities):
    """Add up the study, cooking and exercise minutes of the last 7 days."""
    today = date.today()
    one_week_ago = today - timedelta(days=6)
    totals = {"study_min": 0, "cooking_min": 0, "exercise_min": 0}
    for activity in activities:
        activity_date = date.fromisoformat(activity["date"])
        if one_week_ago <= activity_date <= today:
            totals["study_min"] = totals["study_min"] + activity["study_min"]
            totals["cooking_min"] = totals["cooking_min"] + activity["cooking_min"]
            totals["exercise_min"] = totals["exercise_min"] + activity["exercise_min"]
    return totals
