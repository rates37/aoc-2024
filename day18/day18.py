import sys
from collections import deque
from typing import List, Union

GRID_SIZE = 71
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(grid: List[List[str]]) -> Union[int, None]:
    queue = deque([(0, 0, 0)])  # (x, y, step)
    visited = set()
    visited.add((0, 0))

    while queue:
        x, y, step = queue.popleft()

        if (x, y) == (GRID_SIZE - 1, GRID_SIZE - 1):
            return step

        for dx, dy in DIRECTIONS:
            nextX, nextY = x + dx, y + dy
            if (
                0 <= nextX < GRID_SIZE
                and 0 <= nextY < GRID_SIZE
                and (nextX, nextY) not in visited
                and grid[nextX][nextY] == "."
            ):
                queue.append((nextX, nextY, step + 1))
                visited.add((nextX, nextY))


def part1() -> None:
    # read file:
    with open(sys.argv[1], "r") as f:
        positions = [tuple(map(int, l.strip().split(","))) for l in f]
    grid = [list("." * GRID_SIZE) for _ in range(GRID_SIZE)]
    for i in range(1024):
        (x, y) = positions[i]
        grid[x][y] = "#"
    print(bfs(grid))


def part2() -> None:
    with open(sys.argv[1], "r") as f:
        positions = [tuple(map(int, l.strip().split(","))) for l in f]
    grid = [list("." * GRID_SIZE) for _ in range(GRID_SIZE)]
    for x, y in positions:
        grid[x][y] = "#"
        if bfs(grid) is None:
            print(f"{x},{y}")
            break


if __name__ == "__main__":
    part1()

    part2()
