#!/usr/bin/env python3

import sys
from util import Grid

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

g = Grid(xs)

antis = set()
for v, ps in g.points_by_value().items():
    if v == ".":
        continue

    for p in ps:
        for o in ps:
            if o == p:
                continue

            d = (p.x - o.x, p.y - o.y)

            anti = p + d

            if anti in g.d:
                antis.add(anti)



print(len(antis))
