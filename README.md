# Placement Readiness Tracker

A small command-line tool for the department placement cell. It records students'
practice-test scores (aptitude, verbal, coding), calculates averages and grades,
finds the top scorer and flags students who need extra practice.

Built for **Industry Readiness Programme-II (CSE2596)**, Assessment 4.

## Features

- Stores students as a list of dictionaries (`name`, `roll_no`, `aptitude`, `verbal`, `coding`)
- Adds new students from the keyboard with `input()`; scores outside 0-100 are rejected in a loop
- `average()`, `grade()`, `top_scorer()` and `needs_practice()` functions
- Prints a neatly formatted result table

Grades: **A** (average 80+), **B** (60+), **C** (40+), otherwise **Needs practice**.

## How to run

Requires Python 3.8 or newer. No extra packages are needed.

```bash
python tracker.py
```

(On some systems use `python3 tracker.py`.)

The program asks you to add a student, then prints the result table, the top scorer
and the students who need extra practice.

### Runner-up score (Task 3)

```bash
python runner_up.py          # type: 5 then 70 85 85 60 90   -> prints 85
python test_runner_up.py     # runs my own test cases
```

## Sample output

```
=== Placement Readiness Tracker ===

Add a new student
Enter student name: Meera Nair
Enter roll number: CS106
Enter aptitude score (0-100): 150
  Score must be between 0 and 100. Try again.
Enter aptitude score (0-100): 88
Enter verbal score (0-100): 77
Enter coding score (0-100): 91
Added Meera Nair (CS106).

Add another student? (y/n): n

--- Result table ---
Roll No  Name              Apt  Verbal  Coding     Avg  Grade
-------------------------------------------------------------------------
CS101    Aarav Sharma       82      76      91   83.00  A
CS102    Diya Patel         65      70      58   64.33  B
CS103    Rohan Mehta        45      52      48   48.33  C
CS104    Sneha Iyer         30      38      25   31.00  Needs practice
CS105    Kabir Singh        90      85      95   90.00  A
CS106    Meera Nair         88      77      91   85.33  A

Top scorer: Kabir Singh (CS105) with an average of 90.00

Students who need extra practice (average below 40):
  - Sneha Iyer (CS104): 31.00
```

## Project files

| File | Purpose |
|------|---------|
| `tracker.py` | Main program (Tasks 1 and 2) |
| `runner_up.py` | Runner-up score solution (Task 3) |
| `test_runner_up.py` | Test cases for Task 3 |
| `analysis.md` | Short analysis (Task 5) |

## Git workflow

Work was done on a `feature-grades` branch (average, grade, top scorer and
needs-practice functions) and merged into `main`.
