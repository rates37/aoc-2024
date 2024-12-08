import sys
from itertools import combinations


def part1() -> None:
    # read in data:
    lines = [l.strip() for l in open(sys.argv[1], "r").readlines()]
    antennas = {}
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char != ".":
                if char not in antennas.keys():
                    antennas[char] = []
                antennas[char].append((i, j))
    width = len(lines[0])
    height = len(lines)

    antiNodes = set()

    # consider every type of antenna
    for c in antennas:
        nodes = antennas[c]
        # consider every 2-combination of this type of antenna
        for a1, a2 in combinations(nodes, 2):
            dx = a1[0] - a2[0]
            dy = a1[1] - a2[1]

            if 0 <= a1[0] + dx < height and 0 <= a1[1] + dy < width:
                antiNodes.add((a1[0] + dx, a1[1] + dy))
            if 0 <= a2[0] - dx < height and 0 <= a2[1] - dy < width:
                antiNodes.add((a2[0] - dx, a2[1] - dy))
    print(len(antiNodes))


def part2() -> None:
    # read in data:
    lines = [l.strip() for l in open(sys.argv[1], "r").readlines()]
    antennas = {}
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char != ".":
                if char not in antennas.keys():
                    antennas[char] = []
                antennas[char].append((i, j))
    width = len(lines[0])
    height = len(lines)

    antiNodes = set()

    # consider every type of antenna
    for c in antennas:
        nodes = antennas[c]
        # consider every 2-combination of this type of antenna
        for a1, a2 in combinations(nodes, 2):
            dx = a1[0] - a2[0]
            dy = a1[1] - a2[1]

            # loop until each point is out of grid:
            while 0 <= a1[0] < height and 0 <= a1[1] < width:
                antiNodes.add((a1[0], a1[1]))
                a1 = (a1[0] + dx, a1[1] + dy)

            while 0 <= a2[0] < height and 0 <= a2[1] < width:
                antiNodes.add((a2[0], a2[1]))
                a2 = (a2[0] - dx, a2[1] - dy)

    print(len(antiNodes))


if __name__ == "__main__":
    part1()

    part2()
