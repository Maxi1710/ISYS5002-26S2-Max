# Energy Planner for Shift Work

A command-line Python program that predicts how much energy I will have after a shift at the flower farm and suggests a realistic plan for studying, cooking and exercising in the time left before bed.

## Rationale

I work five days a week at a flower farm while studying: Monday, Tuesday, Thursday, Friday and Saturday. On Mondays and Saturdays I select flowers for customers' orders, and on the other days I deliver them, driving a Sprinter van or a small or medium Isuzu truck. Every shift involves lifting buckets and boxes, so what decides how tired I end up is not the type of task but the number of hours.

Mondays and Tuesdays are my heaviest days. I have worked 10 to 12 hours on them, and on those days I could not exercise, attend classes or cook properly. My usual meal was simply chicken with rice.

A fixed timetable does not work for me, because my energy after a 12-hour Monday is very different from my energy after a shorter day. This program uses my own shift records to predict how much energy I will have after work, and suggests a plan for studying, cooking and exercising that fits the time left before I go to bed at 10 pm.

My goal is to give more time to my studies and to improve my health through better food and regular exercise. The same idea could help other students who balance their degree with physical shift work.

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
| 3. Today's recommendation | Asks when today's shift starts and ends, predicts your energy from past shifts of a similar length (within 1 hour), and suggests a plan that fits your free time before bed. |
| 4. View summary | Shows the average hours and energy for each shift type, and your minutes of the last 7 days against your weekly goals. |
| 5. Exit | Closes the program. |

Every question is validated: an invalid date, time or number is asked again instead of crashing the program.

### Example session

The run below uses test data: one 12-hour sorting shift and two delivery shifts of 11 and 8 hours.

```
=== Energy planner ===
1. Log a shift
2. Log today's activities
3. Today's recommendation
4. View summary
5. Exit
Choose an option: 3

--- Today's recommendation ---
What time do you start? (HH:MM): 05:00
What time do you finish? (HH:MM): 16:00

Based on 2 shift(s) of about 11.0 hours.
Expected energy: 1.5/5 (low)
Free time before bed: 320 min

Suggested plan:
  Study    30 min - Light review of lecture notes
  Cooking  20 min - Something quick: fried chicken or beef with rice and avocado
  Exercise 30 min - Back and leg stretches

=== Energy planner ===
1. Log a shift
2. Log today's activities
3. Today's recommendation
4. View summary
5. Exit
Choose an option: 4

--- Summary ---
delivery: 2 shift(s), 9.5 h average, energy 2.5/5
sorting: 1 shift(s), 12.0 h average, energy 1.0/5

Last 7 days (done / goal):
  Study: 60 / 360 min
  Cooking: 0 / 240 min
  Exercise: 30 / 480 min

=== Energy planner ===
1. Log a shift
2. Log today's activities
3. Today's recommendation
4. View summary
5. Exit
Choose an option: 5
See you later!
```

### Configuration

All adjustable values are in `config.py`. They are set to my own routine:

| Setting | My value | Why |
|---|---|---|
| `BEDTIME` | `"22:00"` | I normally go to bed at 10 pm. |
| `REST_MINUTES` | `40` | After a shift I need about 40 minutes to rest before I can start anything. |
| `DEFAULT_ENERGY` | `3` | A medium energy is used when there are no past shifts of a similar length yet. |
| `HOURS_MARGIN` | `1` | A past shift counts as similar if its length is within 1 hour of today's shift. |
| `LOW_ENERGY_MAX`, `HIGH_ENERGY_MIN` | `2`, `4` | Energy 1-2 is low, 3 is medium, 4-5 is high. |
| `PLANS` | see `config.py` | Minutes and ideas for study, cooking and exercise at each energy level. On a low-energy day the quick meal is fried chicken or beef with rice and avocado. |
| `WEEKLY_GOALS` | study 360, cooking 240, exercise 480 (minutes) | 6 hours of study outside my 10 hours of classes, 2 well-prepared cooking sessions of 2 hours, and 4 gym sessions of 2 hours. |

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

## Known limitations

- The recommendation is for work days only; it does not plan days off.
- Only the time after a shift is counted. Free time before a late shift is ignored.
- A shift that ends after midnight is not handled: its end time would be read as early morning.
- If a shift ends at or after bedtime, the program reports no free time and suggests no plan.
- The prediction is an average of similar shifts, so it is rough until several shifts are logged.

## Open-source acknowledgements

This program does not use any external (third-party) packages. It only uses modules from the Python standard library (`csv`, `datetime`, `pathlib`), which are distributed with Python under the [Python Software Foundation License](https://docs.python.org/3/license.html).

## Sociotechnical considerations

### 1. Separating the system of record from the system of insight

*Sociotechnical Topic C: Systems, scope, and value propositions*

The code keeps the facts and the analysis in separate modules. `storage.py` only saves and reads what happened (each shift, its hours and my energy at the end), so the CSV files work as a **system of record**. `analysis.py` and the summary option turn those records into a **system of insight**: averages by shift type, weekly totals against my goals, and a predicted energy level.

This separation matters because insight should come from real records, not from assumptions. Logging my shifts already displaced one of my own assumptions: I expected delivery and sorting days to feel different, but both involve lifting buckets and boxes, and what really drains my energy is the number of hours. Because the records are kept apart from the analysis, I could change the prediction to use shift length instead of shift type without losing any history.

### 2. A decision support system that suggests, but does not decide

*Sociotechnical Topic C: Systems, scope, and value propositions*

The program is a **decision support system**: it suggests a plan, but the decision stays with me. `recommender.py` returns a *suggested* plan, and `main.py` shows the evidence behind it ("Based on 2 shift(s) of about 11.0 hours", or a warning that there is no history yet and a default energy is being used). When the plan does not fit my free time before bed, it is reduced instead of asking for the impossible.

As the lectures stressed, a DSS supports a decision, but it is the human's job to take responsibility for it. A tool that gave orders, or hid how it reached them, could push me to overwork after a 12-hour shift. Showing the basis of each suggestion lets me judge it and ignore it when my body says otherwise.

### 3. Using only data I enter myself

*Sociotechnical Topic D: Ethics of web scraping*

The program only uses data that I type in myself; it does not collect information from websites or other people. Following the MoSCoW technique, web scraping was a deliberate "won't have": the lectures showed the legal and ethical risks of scraping, and my problem does not need external data.
