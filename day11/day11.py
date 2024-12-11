import sys
from typing import List
from collections import defaultdict


def part1() -> None:
    # read input:
    with open(sys.argv[1], "r") as file:
        stones = file.read().strip().split()

    # function to blink:
    def blink(stones: List[str]) -> List[str]:
        newStones = []

        for s in stones:
            if s == "0":
                newStones.append("1")
            elif len(s) % 2 == 0:  # even so split
                m = len(s) // 2
                l, r = s[:m], s[m:]

                l = str(int(l))
                r = str(int(r))

                newStones.append(l)
                newStones.append(r)
            else:
                newStones.append(str(int(s) * 2024))
        return newStones

    for _ in range(25):
        stones = blink(stones)

    print(len(stones))


def part2() -> None:
    # read input:
    with open(sys.argv[1], "r") as file:
        stones = file.read().strip().split()

    stones: defaultdict = {s: 1 for s in stones}

    # function to blink:
    def blink(stones: defaultdict[int]) -> defaultdict[int]:
        newStones = defaultdict(int)
        for s in stones.keys():
            if s == "0":
                newStones["1"] += stones[s]
            elif len(s) % 2 == 0:
                newStones[str(int(s[: len(s) // 2]))] += stones[s]
                newStones[str(int(s[len(s) // 2 :]))] += stones[s]
            else:
                newStones[str(int(s) * 2024)] += stones[s]
        return newStones

    for _ in range(75):
        stones = blink(stones)

    print(sum(stones.values()))


if __name__ == "__main__":
    part1()

    part2()
