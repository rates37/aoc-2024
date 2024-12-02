import sys
from typing import List

def is_safe(line: List[int]) -> bool:
    increasing = all(line[i] < line[i + 1] for i in range(len(line) - 1))
    decreasing = all(line[i] > line[i + 1] for i in range(len(line) - 1))

    if not (increasing or decreasing):
        return False

    # Check difference between adjacent entries
    for i in range(len(line) - 1):
        if not 1 <= abs(line[i] - line[i + 1]) <= 3:
            return False
    return True


def check_with_removed(line: List[int]) -> bool:
    # Try removing one entry at a time
    for i in range(len(line)):
        newLine = line[:]
        newLine.pop(i)
        if is_safe(newLine):
            return True
    return False


def part1() -> None:
    # Read the input file
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    safeCount = 0

    for line in lines:
        line = list(map(int, line.split()))

        if is_safe(line):
            safeCount += 1
    print(safeCount)


def part2() -> None:
    # Read the input file
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    safeCount = 0

    for line in lines:
        line = list(map(int, line.split()))

        if is_safe(line) or check_with_removed(line):
            safeCount += 1
    print(safeCount)


if __name__ == "__main__":
    part1()

    part2()
