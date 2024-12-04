#!/usr/bin/env python3

import sys
from util import Grid, ADJACENT

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

g = Grid(xs)

def ray(grid, point, direction):
    p = point + direction
    out = ""
    for _ in range(3):
        if p not in grid:
            break
        out += grid[p]
        p += direction

    return out


t = 0
for p in g.points_by_value()["X"]:
    for dir in ADJACENT:
        t += ray(g, p, dir) == "MAS"

print(t)
