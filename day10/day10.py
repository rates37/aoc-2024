import sys
from collections import deque
from typing import List, Set, Tuple


def part1() -> None:
    # read input:
    with open(sys.argv[1], "r") as f:
        grid = [list(map(int, line.strip())) for line in f.readlines()]

    maxX = len(grid)
    maxY = len(grid[0])

    # function to check if valid:
    def is_valid_move(x: int, y: int, maxX: int, maxY: int) -> bool:
        return 0 <= x < maxX and 0 <= y < maxY

    # bfs:
    def bfs(grid: List[List[int]], startX: int, startY: int) -> int:
        dirns = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        q = deque([(startX, startY)])
        visited = set([(startX, startY)])
        score = 0

        while len(q) > 0:
            currX, currY = q.popleft()

            if grid[currX][currY] == 9:
                score += 1

            for dx, dy in dirns:
                nextX = currX + dx
                nextY = currY + dy

                if (
                    is_valid_move(nextX, nextY, maxX, maxY)
                    and (nextX, nextY) not in visited
                ):
                    if grid[nextX][nextY] == grid[currX][currY] + 1:
                        visited.add((nextX, nextY))
                        q.append((nextX, nextY))
        return score

    totalScore = 0

    for x in range(maxX):
        for y in range(maxY):
            if grid[x][y] == 0:
                totalScore += bfs(grid, x, y)
    print(totalScore)


def part2() -> None:
    # read input:
    with open(sys.argv[1], "r") as f:
        grid = [list(map(int, line.strip())) for line in f.readlines()]

    maxX = len(grid)
    maxY = len(grid[0])

    # function to check if valid:
    def is_valid_move(x: int, y: int, maxX: int, maxY: int) -> bool:
        return 0 <= x < maxX and 0 <= y < maxY

    def dfs(
        grid: List[List[int]], startX: int, startY: int, visited: Set[Tuple[int]]
    ) -> int:
        if grid[startX][startY] == 9:
            return 1

        dirns = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        score = 0

        # set this node as active
        visited.add((startX, startY))

        for dx, dy in dirns:
            nextX = startX + dx
            nextY = startY + dy

            if (
                is_valid_move(nextX, nextY, maxX, maxY)
                and (nextX, nextY) not in visited
            ):
                if grid[nextX][nextY] == grid[startX][startY] + 1:
                    score += dfs(grid, nextX, nextY, visited)
        # set this node as inactive
        visited.remove((startX, startY))

        return score

    totalScore = 0

    for x in range(maxX):
        for y in range(maxY):
            if grid[x][y] == 0:
                visited = set()
                totalScore += dfs(grid, x, y, visited)
    print(totalScore)


if __name__ == "__main__":
    part1()

    part2()
