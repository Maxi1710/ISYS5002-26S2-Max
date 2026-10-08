"""Storage: saves and reads the data in CSV files.

This file does not ask the user anything and does not do any calculations.
"""

import csv

import config


def prepare_file(path, columns):
    """Create the folder and the CSV with its header row if they do not exist."""
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        with open(path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()


def save_row(path, columns, row):
    """Append one row (a dictionary) to the end of a CSV."""
    prepare_file(path, columns)
    with open(path, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writerow(row)


def read_rows(path, columns):
    """Return every row of a CSV as a list of dictionaries."""
    prepare_file(path, columns)
    with open(path, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def save_shift(shift):
    """Save one work shift."""
    save_row(config.SHIFTS_FILE, config.SHIFT_COLUMNS, shift)


def read_shifts():
    """Return every shift, with the energy converted to a number."""
    shifts = read_rows(config.SHIFTS_FILE, config.SHIFT_COLUMNS)
    for shift in shifts:
        shift["energy"] = int(shift["energy"])
    return shifts


def save_activity(activity):
    """Save the activities of one day (study, cooking, exercise)."""
    save_row(config.ACTIVITIES_FILE, config.ACTIVITY_COLUMNS, activity)


def read_activities():
    """Return every activity, with the minutes converted to numbers."""
    activities = read_rows(config.ACTIVITIES_FILE, config.ACTIVITY_COLUMNS)
    for activity in activities:
        activity["study_min"] = int(activity["study_min"])
        activity["cooking_min"] = int(activity["cooking_min"])
        activity["exercise_min"] = int(activity["exercise_min"])
    return activities
