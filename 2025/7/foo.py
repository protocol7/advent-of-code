#!/usr/bin/env python3

import sys
from util import Grid, E, S, W

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

g = Grid(xs)

ps = g.points_by_value()["S"]

t = 0
for _ in range(len(xs)):
    nps = []
    for p in ps:
        np = p + S

        v = g[np]

        if v == "^":
            nps.append(np + W)
            nps.append(np + E)
            t += 1
        else:
            nps.append(np)

    ps = set(nps)

print(t)
