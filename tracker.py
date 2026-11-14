"""Placement Readiness Tracker.

A small command-line tool that records students' practice-test scores,
calculates results and flags students who need extra practice.
"""

# ---------------------------------------------------------------------------
# Task 1: data stored as a list of dictionaries
# ---------------------------------------------------------------------------
students = [
    {"name": "Aarav Sharma", "roll_no": "CS101", "aptitude": 82, "verbal": 76, "coding": 91},
    {"name": "Diya Patel", "roll_no": "CS102", "aptitude": 65, "verbal": 70, "coding": 58},
    {"name": "Rohan Mehta", "roll_no": "CS103", "aptitude": 45, "verbal": 52, "coding": 48},
    {"name": "Sneha Iyer", "roll_no": "CS104", "aptitude": 30, "verbal": 38, "coding": 25},
    {"name": "Kabir Singh", "roll_no": "CS105", "aptitude": 90, "verbal": 85, "coding": 95},
]

print("Students loaded:", len(students))
for s in students:
    print(s)
