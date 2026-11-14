"""Runner-up score (Task 3).

Input : an integer n, then n scores (0-100).
Output: the second-highest DISTINCT score.
Reads from standard input, so it works on HackerRank / Codeforces style judges.
"""
import sys


def runner_up(scores):
    distinct = sorted(set(scores), reverse=True)  # remove duplicates, high -> low
    return distinct[1]


if __name__ == "__main__":
    data = sys.stdin.read().split()
    n = int(data[0])
    scores = [int(x) for x in data[1:n + 1]]
    print(runner_up(scores))
