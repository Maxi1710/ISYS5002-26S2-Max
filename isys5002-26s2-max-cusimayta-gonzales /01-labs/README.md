# Energy Planner for Shift Work

A command-line Python program that predicts how much energy I will have after a shift at the flower farm and suggests a realistic plan for studying, cooking and exercising in the time left before bed.

<!--
  HOW TO USE THIS TEMPLATE
  - Sections marked "WRITE IN YOUR OWN WORDS" are assessed as your work: delete the guide comments and write the text yourself.
  - Sections without that mark describe the code as it is now. Update them if you change the code.
  - Delete every comment block like this one before submitting.
-->

## Rationale

<!--
  WRITE IN YOUR OWN WORDS (about 150-250 words). Answer these questions:
  - What do you do at the flower farm? (delivery in trucks, sorting flowers: hours, how physical it is)
  - What happens after a hard shift? Give one real example of a day when you got home and did not study, cook or exercise.
  - Why do a delivery shift and a sorting shift leave you with different energy?
  - What does the program change in your routine? Why is a plan based on your own history better than a fixed timetable?
  - Who else could use it? (other students who work shifts)
-->

## Usage

### Requirements

- Python 3.10 or newer
- No external packages: the program only uses the Python standard library.

### Running the program

From the `02-project` folder:

```bash
python main.py
```

The program shows a menu. Type a number and press Enter:

| Option | What it does |
|---|---|
| 1. Log a shift | Saves the date, shift type (delivery or sorting), start and end time, and your energy at the end (1 to 5). |
| 2. Log today's activities | Saves the minutes you spent studying, cooking and exercising. |
| 3. Today's recommendation | Asks which shift you have today and when it ends, predicts your energy from past shifts of the same type, and suggests a plan that fits your free time before bed. |
| 4. View summary | Shows the average hours and energy for each shift type, and your minutes of the last 7 days against your weekly goals. |
| 5. Exit | Closes the program. |

Every question is validated: an invalid date, time or number is asked again instead of crashing the program.

### Example session

<!--
  Paste a real run copied from your terminal here, inside the code block.
  Use test data, not your real routine.
-->

```
=== Energy planner ===
1. Log a shift
2. Log today's activities
3. Today's recommendation
4. View summary
5. Exit
Choose an option: 3
...
```

### Configuration

All adjustable values are in `config.py`:

| Setting | Meaning |
|---|---|
| `BEDTIME` | Time you go to sleep, used to calculate free time |
| `REST_MINUTES` | Minutes to rest after a shift before starting anything |
| `DEFAULT_ENERGY` | Energy used when there are no past shifts of that type |
| `LOW_ENERGY_MAX`, `HIGH_ENERGY_MIN` | Limits between low, medium and high energy |
| `PLANS` | Minutes and ideas for study, cooking and exercise at each energy level |
| `WEEKLY_GOALS` | Weekly minutes you aim for in each activity |

<!-- Explain briefly WHY you chose your own values (for example, why 22:30 or why 25 minutes of study on a low-energy day). -->

### Data files

The program creates a `data/` folder next to the code the first time it runs:

- `data/shifts.csv`: one row per shift (`date, type, start_time, end_time, energy`)
- `data/activities.csv`: one row per day (`date, study_min, cooking_min, exercise_min`)

The `data/` folder is excluded from the repository with `.gitignore`, so personal data is never committed.

### Code structure

| File | Responsibility |
|---|---|
| `main.py` | Menu and main flow; connects the other modules |
| `config.py` | File paths, routine settings, plans and goals |
| `storage.py` | Reads and writes the CSV files |
| `inputs.py` | Asks the user for data and validates it |
| `analysis.py` | Shift duration, energy prediction, free time and summaries |
| `recommender.py` | Turns predicted energy and free time into a plan |

## Open-source acknowledgements

This program does not use any external (third-party) packages. It only uses modules from the Python standard library (`csv`, `datetime`, `pathlib`), which are distributed with Python under the [Python Software Foundation License](https://docs.python.org/3/license.html).

<!-- If you add an external package (for example pandas or rich), list it here: name, official link and licence. -->

## Sociotechnical considerations

<!--
  WRITE IN YOUR OWN WORDS. The specification asks for at least 2 design decisions,
  each linked to a sociotechnical topic FROM THE LECTURES (use the exact name of the topic from your unit).
  For each one write: the decision, where it is in the code, the topic, and why the decision matters.

  Two decisions already in the code that you can use:

  1. Privacy of personal data
     - Code: config.py stores data in data/, and .gitignore keeps that folder out of GitHub.
     - Question to answer: why should a record of your work hours and energy stay private? Who could misuse it?

  2. Suggestions that adapt instead of rules that blame
     - Code: recommender.py reduces the plan when it does not fit your free time,
       and lowers the effort on low-energy days instead of keeping a fixed timetable.
     - Question to answer: how can productivity tools harm wellbeing by pushing people to do more?
       How does this design respect the user's limits?

  If you build the special feature, it can become a third decision.
-->

### 1. <!-- Decision name -->

### 2. <!-- Decision name -->

## Use of generative AI

<!--
  Keep this section honest and complete. Adjust the first paragraph if anything changes,
  and WRITE THE LIST OF YOUR OWN CONTRIBUTIONS YOURSELF.
-->

The initial version of the six Python modules was generated with Claude (Anthropic) during a guided conversation. The full conversation is recorded in the `ai-assistance-logs` folder, following the unit's record-keeping specification.

My own contributions:

<!--
  - Choosing the project idea and adapting it to my job at the flower farm
  - Choosing the values in config.py based on my real routine
  - Fixing ... (for example, the zero-minute plan when a shift ends late)
  - Building the special feature: ...
  - Writing this README, testing the program and recording the video
-->
