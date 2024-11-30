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

start = [p for p in g.points_by_value()["."] if p.x == 0][0]

print(start)

targets = set(g.points_by_value()["P"])
print(targets)

def flood(g, start, targets):
    targets = set(targets)
    seen = set([start])
    curs = [start]
    for time in count(1):
        print(time, curs)
        ncurs = []
        for c in curs:
            for n, nv in g.orthogonal(c):
                if n in seen:
                    continue
                seen.add(n)

                if nv and nv not in ".P":
                    continue

                if n in targets:
                    targets.remove(n)

                if not targets:
                    return time

                ncurs.append(n)

        curs = ncurs

print(flood(g, start, targets))
