#!/usr/bin/env python3

import sys
from collections import *
from itertools import *
from util import *

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

g = Grid(xs)

# the trick is that these are three maps, only connected on the bottom row next to the herbs labeled K
# split into three maps and solve each separately
#
# edited input to make easier to solve

start = g.points_by_value()["."][0]
start_e = g.points_by_value()["E"][0]
start_r = g.points_by_value()["R"][0]

herbs = [['A', 'B', 'C', 'D'], ['G', 'H', 'I', 'J', 'K', "L"], ['N', 'O', 'P', 'Q']]

def is_neighbour(_, __, ___, nv):
    if nv and nv != "#" and nv != "~":
        return True

graph = g.to_graph(start, is_neighbour)

def solve(start, herbs):
    shortest = sys.maxsize
    shortest_path = []
    for hh in permutations(herbs):
        full_path = []
        cur = start
        path_len = 0
        for h in hh:
            path = bfs(graph, cur, lambda x: g[x] == h)

            full_path += path[1:]
            path_len += len(path) - 1
            cur = path[-1]

        path = bfs(graph, cur, start)

        full_path += path[1:]
        path_len += len(path) - 1

        if path_len < shortest:
            shortest = path_len
            shortest_path = full_path

    return shortest, shortest_path

total = 0
total_path = []
for i in range(3):
    l, p = solve([start_e, start, start_r][i], herbs[i])
    total += l
    total_path += p

print(total + 2 * 4)  # 2 * 4 for the gaps between the maps

for p in g.d.keys():
    if p in total_path:
        g.d[p] = "X"
    elif g.d[p] == ".":
        g.d[p] = " "

g.pretty_print()
