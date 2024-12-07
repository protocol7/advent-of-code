#!/usr/bin/env python3

import sys
from collections import *
from itertools import *
from util import *

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

g = Grid(xs)

p = g.points_by_value()["^"][0]
dir = UP

seen = set([p])
while True:
    np = p + dir
    nv = g[np]

    if nv == "#":
        dir = turn_right(dir)
    elif nv is None:
        break
    elif nv in ".^":
        seen.add(np)
        p = np
    else:
        assert False

print(len(seen))

