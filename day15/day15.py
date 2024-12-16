import sys
from typing import Tuple

moveMap = {">": (1, 0), "<": (-1, 0), "v": (0, 1), "^": (0, -1)}


def part1() -> None:
    # read in input:
    with open(sys.argv[1], "r") as f:
        grid, moves = [p.strip() for p in f.read().split("\n\n")]

    grid = [list(l) for l in grid.splitlines()]
    moves = "".join(l for l in moves.splitlines())

    # get robot position:
    robotPosition = None
    for i, line in enumerate(grid):
        for j in range(len(line)):
            if grid[i][j] == "@":
                robotPosition = (i, j)
                grid[i][j] = "."
                break
        if robotPosition is not None:
            break

    for m in moves:
        dj, di = moveMap[m]
        moveToMake = dict()
        canMove = True

        i, j = robotPosition

        while True:
            if grid[i + di][j + dj] == ".":
                moveToMake[(i + di, j + dj)] = grid[i][j]
                break
            elif grid[i + di][j + dj] == "O":
                moveToMake[(i + di, j + dj)] = grid[i][j]
                i += di
                j += dj
            else:
                canMove = False
                break
        if canMove:
            for m in moveToMake:
                x, y = m
                grid[x][y] = moveToMake[m]
            grid[robotPosition[0]][robotPosition[1]] = "."
            robotPosition = (robotPosition[0] + di, robotPosition[1] + dj)
    total = 0

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "O":
                total += x + 100 * y
    print(total)

    pass


def part2() -> None:
    # read in input:
    with open(sys.argv[1], "r") as f:
        grid, moves = [p.strip() for p in f.read().split("\n\n")]

    smallGrid = [list(l) for l in grid.splitlines()]
    moves = "".join(l for l in moves.splitlines())

    # make it all 2x size:
    sizeMap = {"#": "##", "O": "[]", ".": "..", "@": "@."}
    grid = [[] for _ in range(len(smallGrid))]
    for i, l in enumerate(smallGrid):
        for c in l:
            grid[i].extend(list(sizeMap[c]))

    # get robot position:
    robotPosition = None
    for i, line in enumerate(grid):
        for j in range(len(line)):
            if grid[i][j] == "@":
                robotPosition = (i, j)
                break
        if robotPosition is not None:
            break

    for m in moves:
        dj, di = moveMap[m]

        canMove = True
        movesToMake = []
        path = [robotPosition]
        visited = set()

        while path:
            i, j = path.pop()

            if (i, j) in visited or grid[i][j] == ".":
                continue
            visited.add((i, j))

            if grid[i][j] == "#":
                canMove = False
                break

            movesToMake.append((grid[i][j], i, j))
            path.append((i + di, j + dj))

            if grid[i][j] == "[":
                path.append((i, j + 1))
            if grid[i][j] == "]":
                path.append((i, j - 1))

        if not canMove:
            continue

        # make moves in the order they should be taken in:
        if di > 0:
            movesToMake.sort(key=lambda x: x[1])
        if di < 0:
            movesToMake.sort(key=lambda x: -x[1])

        if dj > 0:
            movesToMake.sort(key=lambda x: x[2])
        if di < 0:
            movesToMake.sort(key=lambda x: -x[2])

        while movesToMake:
            c, i, j = movesToMake.pop()
            grid[i + di][j + dj] = c
            grid[i][j] = "."
        robotPosition = (robotPosition[0] + di, robotPosition[1] + dj)

    total = 0

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "[":
                total += x + 100 * y
    print(total)


if __name__ == "__main__":
    part1()

    part2()
