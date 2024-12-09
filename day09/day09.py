import sys
from typing import List, Union


def part1() -> None:
    # read input:
    with open(sys.argv[1], "r") as f:
        content = f.read().strip()

    drive = []
    currentID = 0

    for i, num in enumerate(content):
        length = int(num)

        if i % 2 == 0:  # a file (not empty space)
            for _ in range(length):
                drive.append(str(currentID))
            currentID += 1  # increment the current file id
        else:  # empty space
            for _ in range(length):
                drive.append(".")

    # compress:
    while True:
        try:
            # find next gap:
            nextGap = drive.index(".")
        except:
            break  # if no gap found

        # find file from the right:
        found = False
        for i in range(len(drive) - 1, nextGap + 1, -1):
            if drive[i] != ".":
                # swap:
                drive[nextGap], drive[i] = drive[i], "."
                found = True
                break
        if not found:
            break

    # calculate checksum:
    total = 0
    for i, num in enumerate(drive):
        if num != ".":
            total += i * int(num)
    print(total)


def part2() -> None:
    # read input:
    with open(sys.argv[1], "r") as f:
        content = f.read().strip()

    drive = []
    currentID = 0
    fileIDMap = [] # store length, starting position for each index (file)

    for i, num in enumerate(content):
        length = int(num)

        if i % 2 == 0:  # a file (not empty space)
            fileIDMap.append([length, len(drive)])
            for _ in range(length):
                drive.append(str(currentID))
            currentID += 1  # increment the current file id
        else:  # empty space
            for _ in range(length):
                drive.append(".")

    # function to find free space of at least given length:
    def find_free_space(d: List[str], endIdx: int, length: int) -> Union[int, None]:
        if endIdx == 0:
            return None
        currentLen = None
        currentStart = None
        for i in range(endIdx):
            if currentStart and currentLen >= length:
                return currentStart
            if d[i] == ".":
                if not currentStart:
                    currentStart = i
                    currentLen = 1
                else:
                    currentLen += 1
            else:
                if currentStart and currentLen >= length:
                    return currentStart
                currentStart = False
                currentLen = None
        if currentStart and currentLen >= length:
            return currentStart
        return None

    # compress:
    for id in range(currentID - 1, -1, -1):
        length, startIdx = fileIDMap[id]

        freeSpaceIdx = find_free_space(drive, startIdx, length)

        if freeSpaceIdx is not None:
            for i in range(length):
                drive[i + startIdx] = "."
                drive[i + freeSpaceIdx] = str(id)
            fileIDMap[id][0] = freeSpaceIdx

    # calculate checksum:
    total = 0
    for i, num in enumerate(drive):
        if num != ".":
            total += i * int(num)
    print(total)


if __name__ == "__main__":
    part1()

    part2()
