import sys
from typing import List, Union


def convert_operand(operand: int, regs: List[int]) -> int:
    a, b, c = regs

    if 0 <= operand <= 3:
        return operand
    if operand == 4:
        return a
    if operand == 5:
        return b
    if operand == 6:
        return c


def run_program(regs: List[int], program: List[int]) -> str:
    a, b, c = regs
    pointer = 0
    output = []

    while pointer < len(program):
        opcode, operand = program[pointer : pointer + 2]

        if opcode == 0:  # adv
            a = a >> operand

        elif opcode == 1:  # bxl
            b ^= operand

        elif opcode == 2:  # bst
            b = convert_operand(operand, [a, b, c]) % 8

        elif opcode == 3:  # jnz
            if a != 0:
                pointer = operand
                continue

        elif opcode == 4:  # bxc
            b ^= c

        elif opcode == 5:  # out
            output.append(convert_operand(operand, [a, b, c]) % 8)

        elif opcode == 6:  # bdv
            b = a >> convert_operand(operand, [a, b, c])

        elif opcode == 7:  # cdv
            c = a >> convert_operand(operand, [a, b, c])

        pointer += 2

    return ",".join(map(str, output))


def part1() -> None:
    # read input from file
    regs, prog = open(sys.argv[1], "r").read().strip().split("\n\n")
    a, b, c = list(map(lambda x: int(x.split(" ")[-1]), regs.splitlines()))

    program = list(map(int, prog.strip().split(" ")[-1].split(",")))

    print(run_program([a, b, c], program))


def search(
    a: int, b: int, c: int, program: List[int], currentLen: int
) -> Union[int, None]:
    # base case entire program is outputted
    if len(program) == currentLen - 1:
        return a

    # recursively search:
    ans = []
    for i in range(8):
        newA = (a << 3) | i
        # test if new value of a outputs the last n digits of the program:
        newOutput = list(map(int, run_program([newA, b, c], program).split(",")))
        if newOutput == program[-currentLen:]:
            # recursively search for the value of a that completes the rest of the program
            nextA = search(newA, b, c, program, currentLen + 1)

            # if a value was found, append it to possible answers
            if nextA:
                ans.append(nextA)
    if ans:
        return min(ans)
    else:
        return None


def part2() -> None:
    # read input from file
    _, prog = open(sys.argv[1], "r").read().strip().split("\n\n")
    program = list(map(int, prog.strip().split(" ")[-1].split(",")))

    # run search function to find value of a
    print(search(0, 0, 0, program, 1))


if __name__ == "__main__":
    part1()

    part2()
