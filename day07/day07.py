import sys
import itertools
from typing import List


def eval_expr(numbers: List[int], ops: List[str]) -> int:
    result = numbers[0]
    for i in range(1, len(numbers)):
        if ops[i - 1] == "+":
            result += numbers[i]
        elif ops[i - 1] == "*":
            result *= numbers[i]
        elif ops[i - 1] == "||":
            result = int(str(result) + str(numbers[i]))
    return result


def check_eqn(testValue: int, numbers: List[int], operators: List[str]) -> bool:
    for ops in list(itertools.product(operators, repeat=len(numbers) - 1)):
        if eval_expr(numbers, ops) == testValue:
            return True
    return False


def part1() -> None:
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    total = 0
    for line in lines:
        testValue, numbers = line.split(":")

        testValue = int(testValue.strip())
        numbers = list(map(int, numbers.strip().split()))

        if check_eqn(testValue, numbers, operators=["+", "*"]):
            total += testValue

    print(total)


def part2() -> None:
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    total = 0
    for line in lines:
        testValue, numbers = line.split(":")

        testValue = int(testValue.strip())
        numbers = list(map(int, numbers.strip().split()))

        if check_eqn(testValue, numbers, operators=["+", "*", "||"]):
            total += testValue

    print(total)


if __name__ == "__main__":
    part1()

    part2()
