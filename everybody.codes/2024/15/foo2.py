#!/usr/bin/env python3

import sys
from collections import *
from itertools import *
from util import *


def parse(line):
    return line.strip()


xs = list(map(parse, sys.stdin))

g = Grid(xs)

start = g.points_by_value()["."][0]

herbs = [h for h in g.points_by_value() if h not in ".#~"]

print(herbs)

def is_neighbour(_, __, ___, nv):
    if nv and nv != "#" and nv != "~":
        return True

graph = g.to_graph(start, is_neighbour)

shortest = sys.maxsize
pp = permutations(herbs)
for i, hh in enumerate(pp):
    print(i, i / len(pp), hh)
    cur = start
    path_len = 0
    for h in hh:
        path = bfs(graph, cur, lambda x: g[x] == h)

        path_len += len(path) - 1
        cur = path[-1]

    path = bfs(graph, cur, start)

    path_len += len(path) - 1

    shortest = min(shortest, path_len)

print(shortest)
