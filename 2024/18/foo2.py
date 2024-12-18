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

last_path = None
for x, y in xs[l:]:
    p = Point(x, y)

    del graph[p]
    for n, _ in g.orthogonal(p):
        if n in graph:
            graph[n].remove(p)

    if last_path is None or p in last_path:
        last_path = bfs(graph, start, end)

        if last_path is None:
            print(f"{x},{y}")
            break
