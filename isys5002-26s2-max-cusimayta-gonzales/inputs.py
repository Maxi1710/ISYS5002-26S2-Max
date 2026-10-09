"""Inputs: asks the user for data and validates it."""

from datetime import date, datetime


def ask_date(message):
    """Ask for a date as YYYY-MM-DD. If the user presses Enter, use today."""
    while True:
        text = input(message + " (YYYY-MM-DD, Enter = today): ").strip()
        if text == "":
            return date.today().isoformat()
        try:
            datetime.strptime(text, "%Y-%m-%d")
            return text
        except ValueError:
            print("Invalid date. Example: 2026-10-05")


def ask_time(message):
    """Ask for a time."""
    while True:
        text = input(message + " (HH:MM): ").strip()
        try:
            time = datetime.strptime(text, "%H:%M")
            return time.strftime("%H:%M")
        except ValueError:
            print("Invalid time. Example: 06:30")


def ask_integer(message, minimum, maximum):
    """Ask for a whole number between minimum and maximum."""
    while True:
        text = input(message + " (" + str(minimum) + "-" + str(maximum) + "): ").strip()
        if text.isdigit():
            number = int(text)
            if minimum <= number <= maximum:
                return number
        print("Enter a number between " + str(minimum) + " and " + str(maximum) + ".")


def ask_option(message, options):
    """Show a numbered list and return the chosen option."""
    print(message)
    number = 1
    for option in options:
        print("  " + str(number) + ". " + option)
        number = number + 1
    chosen = ask_integer("Choose", 1, len(options))
    return options[chosen - 1]
