import sys
import networkx as nx

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def part1() -> None:
    with open(sys.argv[1], "r") as f:
        lines = [l.strip() for l in f.readlines()]

    g = nx.DiGraph()

    # add nodes to graph
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "#":
                continue
            pos = (i, j)

            if c == "S":
                startPos = (pos, (0, 1))
            if c == "E":
                endPos = pos
            for d in directions:
                g.add_node((pos, d))
    # add edges:
    for pos, d in g.nodes:
        nextPos = (pos[0] + d[0], pos[1] + d[1])

        if (nextPos, d) in g.nodes:
            g.add_edge((pos, d), (nextPos, d), weight=1)

        for dd in directions:
            newD = (d[0] * dd[0] - d[1] * dd[1], d[0] * dd[1] + d[1] * dd[0])
            g.add_edge((pos, d), (pos, newD), weight=1000)
    endNode = "end"
    for d in directions:
        g.add_edge((endPos, d), endNode, weight=0)

    print(nx.shortest_path_length(g, startPos, endNode, weight="weight"))


def part2() -> None:
    with open(sys.argv[1], "r") as f:
        lines = [l.strip() for l in f.readlines()]

    g = nx.DiGraph()

    # add nodes to graph
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "#":
                continue
            pos = (i, j)

            if c == "S":
                startPos = (pos, (0, 1))
            if c == "E":
                endPos = pos
            for d in directions:
                g.add_node((pos, d))
    # add edges:
    for pos, d in g.nodes:
        nextPos = (pos[0] + d[0], pos[1] + d[1])

        if (nextPos, d) in g.nodes:
            g.add_edge((pos, d), (nextPos, d), weight=1)

        for dd in directions:
            newD = (d[0] * dd[0] - d[1] * dd[1], d[0] * dd[1] + d[1] * dd[0])
            g.add_edge((pos, d), (pos, newD), weight=1000)
    endNode = "end"
    for d in directions:
        g.add_edge((endPos, d), endNode, weight=0)

    uniquePositions = set()
    for path in nx.all_shortest_paths(g, startPos, endNode, weight="weight"):
        for pos in path:
            uniquePositions.add(pos[0])
    print(len(uniquePositions) - 1)


if __name__ == "__main__":
    part1()

    part2()
