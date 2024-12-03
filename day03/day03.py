import re
import sys


def part1() -> None:
    # Read the input file
    with open(sys.argv[1], "r") as f:
        content = f.read()

    mulPattern = r"mul\((\d+),(\d+)\)"
    totalMultSum = 0

    i = 0
    while i < len(content):
        if content[i : i + 3] == "mul":
            match = re.match(mulPattern, content[i:])
            if match:
                x = int(match.group(1))
                y = int(match.group(2))

                totalMultSum += x * y
                i += match.end()
            else:
                i += 1
        else:
            i += 1

    print(totalMultSum)


def part2() -> None:
    # Read the input file
    with open(sys.argv[1], "r") as f:
        content = f.read()

    mulPattern = r"mul\((\d+),(\d+)\)"
    totalMultSum = 0
    isEnabled = True

    i = 0
    while i < len(content):
        if content[i : i + 3] == "mul":
            match = re.match(mulPattern, content[i:])
            if match:
                x = int(match.group(1))
                y = int(match.group(2))

                if isEnabled:
                    totalMultSum += x * y
                i += match.end()
            else:
                i += 1
        elif content[i : i + len("do()")] == "do()":
            isEnabled = True
            i += len("do()")
        elif content[i : i + len("don't()")] == "don't()":
            isEnabled = False
            i += len("don't()")
        else:
            i += 1

    print(totalMultSum)


if __name__ == "__main__":

    part1()

    part2()
