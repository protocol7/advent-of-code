#!/usr/bin/env python3

import sys
from collections import *
from itertools import *
from util import *


def parse(line):
    return line.strip()


xs = list(map(parse, sys.stdin))

g = Grid(xs)

g.pretty_print()

start = g.points_by_value()["."][0]

def is_neighbour(_, __, ___, nv):
    if nv and nv != "#":
        return True

graph = g.to_graph(start, is_neighbour)

path = bfs(graph, start, lambda x: g[x] == "H")

print(path)
print((len(path) - 1) * 2)
