#!/usr/bin/env python3

import sys
from util import Grid, LEFT, RIGHT, UP, DOWN

def parse(line):
    return line.strip()

a, b = sys.stdin.read().strip().split("\n\n")

a = a.split("\n")

g = Grid(a)

moves = b.replace("\n", "")

start = g.points_by_value()["@"][0]
g.d[start] = "."

dirs = {
    "<": LEFT,
    "^": UP,
    ">": RIGHT,
    "v": DOWN,
}

def try_move(ray):
    # find first non box
    for i, (bp, bv) in enumerate(ray):
        if bv == "#":
            return []
        elif bv == "O":
            continue
        elif bv == ".":
            ray = list(map(list, ray))
            ray[0][1] = "."
            ray[i][1] = "O"

            return ray

p = start
for d in moves:
    dir = dirs[d]

    np = p + dir
    nv = g[np]

    if nv == "#":
        continue
    elif nv == ".":
        p = np
    elif nv == "O":
        r = g.ray(p, dir)

        r = try_move(r)

        if r:
            for rp, rv in r:
                g.d[rp] = rv

            nv = g[np]

            p = np

t = 0
for b in g.points_by_value()["O"]:
    x, y = b
    t += y * 100 + x

print(t)
