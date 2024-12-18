#!/usr/bin/env python3

import sys
from util import ints, Grid, Point, bfs

def parse(line):
    return ints(line.strip())

xs = list(map(parse, sys.stdin))

w = int(sys.argv[1])
h = int(sys.argv[2])
l = int(sys.argv[3])

d = {}
for r in range(h+1):
    for c in range(w+1):
        d[(c, r)] = '.'

for x, y in xs[:l]:
    d[(x, y)] = "#"

g = Grid(d)

start = Point(0, 0)
end = Point(w, h)

def is_neighbour(p, v, np, nv):
    return nv == '.'

graph = g.to_graph(start, is_neighbour)

path = bfs(graph, start, end)

print(len(path) - 1)
