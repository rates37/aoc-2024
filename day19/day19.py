import sys
from functools import lru_cache
from typing import Tuple


@lru_cache(None)
def solve(patterns: Tuple[str], design: str) -> int:
    if design == "":
        return 1
    for p in patterns:
        if design.startswith(p):
            if solve(patterns, design[len(p) :]) > 0:
                return 1
    return 0


def part1() -> None:
    with open(sys.argv[1], "r") as f:
        lines = f.read().strip().split("\n")

    patterns = tuple(lines[0].split(", "))
    designs = lines[2:]

    print(sum(solve(patterns, design) for design in designs))


@lru_cache(None)
def solve_part_2(patterns: Tuple[str], design: str) -> int:
    if design == "":
        return 1
    total = 0
    for p in patterns:
        if design.startswith(p):
            total += solve_part_2(patterns, design[len(p) :])
    return total


def part2() -> None:
    with open(sys.argv[1], "r") as f:
        lines = f.read().strip().split("\n")

    patterns = tuple(lines[0].split(", "))
    designs = lines[2:]

    print(sum(solve_part_2(patterns, design) for design in designs))


if __name__ == "__main__":
    part1()

    part2()
