#!/usr/bin/env python3

import sys
from collections import *
from itertools import *
from util import *


def parse(line):
    return line.strip()


xs = list(map(parse, sys.stdin))

g = Grid(xs)

starts = [p for p in g.points_by_value()["."] if p.x == 0 or p.x == len(xs[0])-1]

targets = set(g.points_by_value()["P"])

def flood(g, starts, targets):
    targets = set(targets)
    seen = set(starts)
    curs = list(starts)
    for time in count(1):
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

print(flood(g, starts, targets))
