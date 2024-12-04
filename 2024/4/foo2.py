#!/usr/bin/env python3

import sys
from util import *

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

g = Grid(xs)

DIRS = [
    [NW, NE, SE, SW],
    [NE, SE, SW, NW],
    [SE, SW, NW, NE],
    [SW, NW, NE, SE],
]

t = 0
for x in g.points_by_value()["A"]:
    for dirs in DIRS:
        s = ""
        for d in dirs:
            v = g[x + d]
            if v:
                s += v

        t += s == "MMSS"

print(t)

