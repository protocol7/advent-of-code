#!/usr/bin/env python3

import sys
from util import Grid, bfs, manhattan

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

g = Grid(xs)

start = g.points_by_value()["S"][0]
end = g.points_by_value()["E"][0]

g.d[start] = "."
g.d[end] = "."

def is_neighbour(p, v, np, nv):
    return nv == "."

graph = g.to_graph(start, is_neighbour)

path = bfs(graph, start, end)

def cheats(limit):
    t = 0
    for i, p in enumerate(path):
        for j, p2 in enumerate(path[i:]):
            m = manhattan(p, p2)
            if m <= limit:
                t += j - m >= 100

    return t

print(cheats(2))
print(cheats(20))
