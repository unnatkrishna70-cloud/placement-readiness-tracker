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


def read_score(subject):
    """Keep asking until the user types a whole number between 0 and 100."""
    while True:
        text = input(f"Enter {subject} score (0-100): ")
        try:
            value = int(text)  # input() returns a string, so convert it
        except ValueError:
            print("  Please enter a whole number.")
            continue
        if 0 <= value <= 100:
            return value
        print("  Score must be between 0 and 100. Try again.")


def add_student(student_list):
    """Read one student from the keyboard and add it to the list."""
    name = input("Enter student name: ").strip()
    roll_no = input("Enter roll number: ").strip()
    student = {
        "name": name,
        "roll_no": roll_no,
        "aptitude": read_score("aptitude"),
        "verbal": read_score("verbal"),
        "coding": read_score("coding"),
    }
    student_list.append(student)
    print(f"Added {name} ({roll_no}).")


add_student(students)
print(f"Total students: {len(students)}")
