from collections import defaultdict
import sys
from math import floor, ceil


def part1() -> None:
    with open(sys.argv[1], "r") as f:
        lines = [l.strip() for l in f.readlines()]

    robots = []
    for l in lines:
        pos, vel = l.strip().split(" v=")
        pos = tuple(map(int, pos[2:].split(",")))
        vel = tuple(map(int, vel.split(",")))
        robots.append((pos, vel))

    width = 101
    height = 103
    time = 100

    grid = [[0] * width for _ in range(height)]

    for (px, py), (vx, vy) in robots:
        grid[(py + vy * time) % height][(px + vx * time) % width] += 1

    midX = width // 2
    midY = height // 2

    q1, q2, q3, q4 = 0, 0, 0, 0

    for y in range(height):
        for x in range(width):
            if x == midX or y == midY:
                continue  # Skip center lines
            if x < midX and y < midY:
                q1 += grid[y][x]
            elif x > midX and y < midY:
                q2 += grid[y][x]
            elif x < midX and y > midY:
                q3 += grid[y][x]
            elif x > midX and y > midY:
                q4 += grid[y][x]
    print(q1 * q2 * q3 * q4)


def part2() -> None:
    with open(sys.argv[1], "r") as f:
        lines = [l.strip() for l in f.readlines()]

    robots = []
    for l in lines:
        pos, vel = l.strip().split(" v=")
        pos = tuple(map(int, pos[2:].split(",")))
        vel = tuple(map(int, vel.split(",")))
        robots.append((pos, vel))

    width = 101
    height = 103
    time = 1

    # find the first time no robots are in the same position
    while True:
        positions = defaultdict(bool)
        overlap = False

        for (px, py), (vx, vy) in robots:
            newX = (px + vx * time) % width
            newY = (py + vy * time) % height
            if positions[(newX, newY)]:
                overlap = True
                break
            positions[(newX, newY)] = True
        if not overlap:
            break

        time += 1
    print(time)


if __name__ == "__main__":
    part1()

    part2()
