"""Main: shows the menu and connects the other modules."""

import analysis
import config
import inputs
import recommender
import storage

def show_menu():
    """Print the main menu."""
    print("\n=== Energy planner ===")
    print("1. Log a shift")
    print("2. Log today's activities")
    print("3. Today's recommendation")
    print("4. View summary")
    print("5. Exit")

def log_shift():
    """Option 1: details of a shift and save it."""
    print("\n--- Log a shift ---")
    shift = {
        "date": inputs.ask_date("Shift date"),
        "type": inputs.ask_option("Shift type:", config.SHIFT_TYPES),
        "start_time": inputs.ask_time("Start time"),
        "end_time": inputs.ask_time("End time"),
        "energy": inputs.ask_integer("Energy at the end", 1, 5),
    }
    storage.save_shift(shift)
    hours = analysis.duration_in_hours(shift["start_time"], shift["end_time"])
    print("Shift saved: " + shift["type"] + ", " + str(round(hours, 1)) + " hours.")

def log_activities():
    """Option 2: study, cooking and exercise minutes and save them."""
    print("\n--- Log activities ---")
    activity = {
        "date": inputs.ask_date("Date"),
        "study_min": inputs.ask_integer("Minutes of study", 0, 600),
        "cooking_min": inputs.ask_integer("Minutes cooking", 0, 600),
        "exercise_min": inputs.ask_integer("Minutes of exercise", 0, 600),
    }
    storage.save_activity(activity)
    print("Activities saved.")

def show_recommendation():
    """Option 3: predict the energy after today's shift and suggest a plan."""
    print("\n--- Today's recommendation ---")
    start_time = inputs.ask_time("What time do you start?")
    end_time = inputs.ask_time("What time do you finish?")
    hours = analysis.duration_in_hours(start_time, end_time)

    shifts = storage.read_shifts()
    energy, count = analysis.predict_energy(shifts, hours)
    free = analysis.free_minutes(end_time)
    plan = recommender.create_plan(energy, free)

    if count == 0:
        print("\nNo shifts of about " + str(round(hours, 1)) + " hours logged yet; using a medium energy.")
    else:
        print("\nBased on " + str(count) + " shift(s) of about " + str(round(hours, 1)) + " hours.")
    print("Expected energy: " + str(round(energy, 1)) + "/5 (" + plan["level"] + ")")
    print("Free time before bed: " + str(free) + " min")
    if free == 0:
        print("No free time today: rest and go to bed.")
        return
    if plan["was_reduced"]:
        print("The plan was reduced to fit your free time.")

    print("\nSuggested plan:")
    print("  Study    " + str(plan["study_min"]) + " min - " + plan["study_idea"])
    print("  Cooking  " + str(plan["cooking_min"]) + " min - " + plan["cooking_idea"])
    print("  Exercise " + str(plan["exercise_min"]) + " min - " + plan["exercise_idea"])

def show_summary():
    """Option 4: show averages by shift type and weekly progress."""
    print("\n--- Summary ---")
    shifts = storage.read_shifts()
    summary = analysis.summary_by_type(shifts)
    if len(summary) == 0:
        print("No shifts logged yet.")
    for shift_type in summary:
        data = summary[shift_type]
        print(
            shift_type + ": " + str(data["count"]) + " shift(s), "
            + str(round(data["average_hours"], 1)) + " h average, energy "
            + str(round(data["average_energy"], 1)) + "/5"
        )

    print("\nLast 7 days (done / goal):")
    totals = analysis.totals_last_7_days(storage.read_activities())
    names = {"study_min": "Study", "cooking_min": "Cooking", "exercise_min": "Exercise"}
    for key in names:
        goal = config.WEEKLY_GOALS[key]
        print("  " + names[key] + ": " + str(totals[key]) + " / " + str(goal) + " min")

def main():
    """Run the menu loop until the user chooses Exit."""
    while True:
        show_menu()
        option = input("Choose an option: ").strip()

        if option == "1":
            log_shift()
        elif option == "2":
            log_activities()
        elif option == "3":
            show_recommendation()
        elif option == "4":
            show_summary()
        elif option == "5":
            print("See you later!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
