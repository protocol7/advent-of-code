#!/usr/bin/env python3

import sys
from collections import *
from itertools import *
from util import *


def parse(line):
    return line.strip()


xs = list(map(parse, sys.stdin))

for x in xs:
    print(x)

g = Grid(xs)

ps = set(g.points_by_value()["P"])

def flood_fill(grid, point):
    q = deque([(point, 0)])
    dists = {}

    while q:
        point, dist = q.popleft()

        pv = grid.d[point]

        # check that we are in the grid
        if pv is None:
            continue

        # check if we are on the boundary
        if pv not in ".P":
            continue

        # check if we are already filled
        if point in dists:
            continue

        # fill
        dists[point] = dist

        # attempt to fill the neighboring positions
        for n in ORTHOGONAL:
            q.append((point + n, dist+1))

    return dists

total_dists = defaultdict(int)
for p in ps:
    dists = flood_fill(g, p)

    for k, v in dists.items():
        if k in ps:
            continue
        total_dists[k] += v

print(min(total_dists.values()))
