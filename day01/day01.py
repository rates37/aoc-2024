from typing import List
import sys
from collections import Counter


def distance_part_1(left: List[int], right: List[int]) -> int:
    left.sort()
    right.sort()

    return sum(abs(l - r) for (l, r) in zip(left, right))


def distance_part_2(left: List[int], right: List[int]):
    rightListCounter = Counter(right)

    return sum(leftNum * rightListCounter[leftNum] for leftNum in left)


def part1() -> None:
    # read in input file
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()
    left = []
    right = []
    for l in lines:
        i1, i2 = [int(x) for x in l.strip().split()]
        left.append(i1)
        right.append(i2)
    print(distance_part_1(left, right))


def part2() -> None:
    # read in input file
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()
    left = []
    right = []
    for l in lines:
        i1, i2 = [int(x) for x in l.strip().split()]
        left.append(i1)
        right.append(i2)
    print(distance_part_2(left, right))


if __name__ == "__main__":
    part1()

    part2()
