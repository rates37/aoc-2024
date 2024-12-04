import sys
from typing import List, Tuple


def find_word_in_dir(
    puzzle: List[str], targetWord: str, i: int, j: int, direction: Tuple[int, int]
) -> bool:
    for k in range(len(targetWord)):
        char = targetWord[k]
        i1 = i + k * direction[0]
        j1 = j + k * direction[1]

        if (
            0 > i1
            or 0 > j1
            or i1 >= len(puzzle)
            or j1 >= len(puzzle[0])
            or puzzle[i1][j1] != char
        ):
            return False
    return True


def part1() -> None:
    # Read the input file
    with open(sys.argv[1], "r") as f:
        puzzle = [l.strip() for l in f.readlines()]

    directions = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
    ]
    count = 0

    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == "X":
                for dirn in directions:
                    if find_word_in_dir(puzzle, "XMAS", i, j, dirn):
                        count += 1
    print(count)


def part2() -> None:
    # Read the input file
    with open(sys.argv[1], "r") as f:
        puzzle = [l.strip() for l in f.readlines()]

    count = 0

    for r in range(1, len(puzzle) - 1):
        for c in range(1, len(puzzle[0]) - 1):
            if puzzle[r][c] == "A":
                # only check if middle is an A
                valid = True
                # check top left - bottom right:
                chars = [puzzle[r - 1][c - 1], puzzle[r + 1][c + 1]]
                if not sorted(chars) == ["M", "S"]:
                    valid = False
                # check bottom left - top right:
                chars = {puzzle[r + 1][c - 1], puzzle[r - 1][c + 1]}
                if not sorted(chars) == ["M", "S"]:
                    valid = False
                if valid:
                    count += 1

    print(count)


if __name__ == "__main__":
    part1()

    part2()
