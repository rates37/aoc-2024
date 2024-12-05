import sys
from typing import List, Dict


# function to check if in order:
def is_in_order(u: List[int], order: Dict[int, List[int]]) -> bool:
    for x in order.keys():
        if x in u:
            for y in order[x]:
                if y in u:
                    xIdx = u.index(x)
                    yIdx = u.index(y)

                    if xIdx > yIdx:
                        return False
    return True


# world's worst top sort implementation:
def top_sort(u: List[int], order: Dict[int, List[int]]) -> List[int]:
    inDegrees = dict()
    for i in u:
        inDegrees[i] = 0

    # count all in-degrees of the vertices in the current u
    for x in order:
        if x in u:
            for y in order[x]:
                if y in u:
                    inDegrees[y] += 1
    # create queue:
    queue = [i for i in u if inDegrees[i] == 0]
    sortedU = []
    while queue:
        i = queue.pop()
        sortedU.append(i)

        for x in order:
            # reduce all the in degrees of other nodes:
            if x == i:
                for y in order[x]:
                    if y in u:
                        inDegrees[y] -= 1
                        if inDegrees[y] == 0:
                            queue.append(y)
    return sortedU


def part1() -> None:
    # Read the input file
    with open(sys.argv[1], "r") as f:
        # read rules:
        rules = []
        while True:
            line = f.readline().strip()

            if not line:
                break
            rules.append(line)
        
        # read updates:
        updates = []
        while True:
            line = f.readline().strip()
            if not line:
                break
            updates.append(list(map(int, line.split(","))))

    # parse rules from read lines:
    order = {}

    for r in rules:
        x, y = map(int, r.split("|"))
        if x not in order.keys():
            order[x] = []
        order[x].append(y)

    # sum up totals:
    count = 0

    for u in updates:
        if is_in_order(u, order):
            count += u[len(u) // 2]
    print(count)


def part2() -> None:
    # Read the input file
    with open(sys.argv[1], "r") as f:
        # read rules:
        rules = []
        while True:
            line = f.readline().strip()

            if not line:
                break
            rules.append(line)
        
        # read updates:
        updates = []
        while True:
            line = f.readline().strip()
            if not line:
                break
            updates.append(list(map(int, line.split(","))))

    # parse rules from read lines:
    order = {}

    for r in rules:
        x, y = map(int, r.split("|"))
        if x not in order.keys():
            order[x] = []
        order[x].append(y)

    # sum up totals:
    count = 0

    for u in updates:
        if not is_in_order(u, order):
            # correct the update by top sorting:
            u = top_sort(u, order)
            count += u[len(u) // 2]

    print(count)


if __name__ == "__main__":
    part1()

    part2()
