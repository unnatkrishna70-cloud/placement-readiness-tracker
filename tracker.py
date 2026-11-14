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


# ---------------------------------------------------------------------------
# Task 2: functions
# ---------------------------------------------------------------------------
def average(student):
    """Return the mean of the three scores."""
    return (student["aptitude"] + student["verbal"] + student["coding"]) / 3


def grade(avg):
    """A for 80+, B for 60+, C for 40+, otherwise 'Needs practice'."""
    if avg >= 80:
        return "A"
    if avg >= 60:
        return "B"
    if avg >= 40:
        return "C"
    return "Needs practice"


def print_table(student_list):
    """Print a neatly formatted result table using a loop."""
    header = (
        f"{'Roll No':<9}{'Name':<16}{'Apt':>5}{'Verbal':>8}"
        f"{'Coding':>8}{'Avg':>8}  Grade"
    )
    print(header)
    print("-" * (len(header) + 12))
    for s in student_list:
        avg = average(s)
        print(
            f"{s['roll_no']:<9}{s['name']:<16}{s['aptitude']:>5}{s['verbal']:>8}"
            f"{s['coding']:>8}{avg:>8.2f}  {grade(avg)}"
        )


def main():
    print("=== Placement Readiness Tracker ===\n")

    print("Add a new student")
    add_student(students)
    while input("\nAdd another student? (y/n): ").strip().lower() == "y":
        add_student(students)

    print("\n--- Result table ---")
    print_table(students)


if __name__ == "__main__":
    main()
