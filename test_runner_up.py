"""Runs runner_up.py on several inputs and prints a table of
input / expected output / actual output (for the Task 3 submission)."""
import subprocess
import sys

CASES = [
    ("5\n70 85 85 60 90\n", "85"),            # sample from the assignment
    ("4\n100 100 99 98\n", "99"),             # top score repeated
    ("6\n50 50 50 40 40 30\n", "40"),         # top score repeated, many duplicates
    ("2\n0 100\n", "0"),                      # smallest allowed n
]

print(f"{'Input':<26}{'Expected':<10}{'Actual':<10}Result")
print("-" * 56)
for given, expected in CASES:
    result = subprocess.run(
        [sys.executable, "runner_up.py"], input=given, capture_output=True, text=True
    )
    actual = result.stdout.strip()
    shown = given.replace("\n", " | ").strip(" |")
    print(f"{shown:<26}{expected:<10}{actual:<10}{'PASS' if actual == expected else 'FAIL'}")
