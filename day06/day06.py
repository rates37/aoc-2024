import sys
from typing import Tuple


def part1() -> None:
    with open(sys.argv[1], "r") as f:
        grid = [l.strip() for l in f.readlines()]

    direction = (-1, 0)  # initial direction upwards
    startingPos = None

    def next_direction(dir: Tuple[int, int]) -> Tuple[int, int]:
        if dir == (-1, 0):
            return (0, 1)

        if dir == (0, 1):
            return (1, 0)

        if dir == (1, 0):
            return (0, -1)

        if dir == (0, -1):
            return (-1, 0)

    # get starting position
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "^":
                startingPos = (i, j)
                break
        if startingPos is not None:
            break

    visited = [[False for _ in range(len(grid))] for __ in range(len(grid[0]))]
    visited[startingPos[0]][startingPos[1]] = True
    currentPosition = startingPos

    while True:
        # step in next direction:
        x, y = currentPosition
        x += direction[0]
        y += direction[1]

        # check if left grid:
        if (not 0 <= x < len(grid)) or (not 0 <= y < len(grid[0])):
            break

        if grid[x][y] == "#":
            # turn right
            direction = next_direction(direction)
            continue  # skip rest of loop and try move again

        # visit position and update current position
        visited[x][y] = True
        currentPosition = (x, y)

    # count visited:
    print(sum(sum(map(int, g)) for g in visited))


def part2() -> None:
    with open(sys.argv[1], "r") as f:
        grid = [l.strip() for l in f.readlines()]

    direction = (-1, 0)  # initial direction upwards
    startingPos = None

    def next_direction(dir: Tuple[int, int]) -> Tuple[int, int]:
        if dir == (-1, 0):
            return (0, 1)

        if dir == (0, 1):
            return (1, 0)

        if dir == (1, 0):
            return (0, -1)

        if dir == (0, -1):
            return (-1, 0)

    # get starting position
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "^":
                startingPos = (i, j)
                break
        if startingPos is not None:
            break

    visited = [[False for _ in range(len(grid))] for __ in range(len(grid[0]))]
    visited[startingPos[0]][startingPos[1]] = True
    currentPosition = startingPos

    while True:
        # step in next direction:
        x, y = currentPosition
        x += direction[0]
        y += direction[1]

        # check if left grid:
        if (not 0 <= x < len(grid)) or (not 0 <= y < len(grid[0])):
            break

        if grid[x][y] == "#":
            # turn right
            direction = next_direction(direction)
            continue  # skip rest of loop and try move again

        # visit position and update current position
        visited[x][y] = True
        currentPosition = (x, y)

        visitedPositions = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j]:
                    visitedPositions.add((i, j))

    def traverse_map(g, visitCountMax: int) -> bool:
        direction = (-1, 0)
        visited = [[False for _ in range(len(g))] for __ in range(len(g[0]))]
        visited[startingPos[0]][startingPos[1]] = True
        currentPosition = startingPos

        visitCount = 0
        while True:
            if visitCount > visitCountMax:
                return True
            # step in next direction:
            x, y = currentPosition
            x += direction[0]
            y += direction[1]

            # check if left grid:
            if (not 0 <= x < len(g)) or (not 0 <= y < len(g[0])):
                return False

            visitCount += 1
            if g[x][y] == "#":
                # turn right
                direction = next_direction(direction)
                continue  # skip rest of loop and try move again

            # visit position and update current position
            visited[x][y] = True
            currentPosition = (x, y)

    obstructions = 0
    gridCpy = [list(g) for g in grid]

    for pos in visitedPositions:
        if pos != startingPos and gridCpy[pos[0]][pos[1]] == ".":
            tempGrid = [row[:] for row in gridCpy]
            tempGrid[pos[0]][pos[1]] = "#"
            if traverse_map(
                tempGrid, len(visitedPositions) * 2
            ):  # 2x max number of iterations in initial grid (1 for each movement, 1 for each turn)
                obstructions += 1
    print(obstructions)


if __name__ == "__main__":

    part1()

    part2()
