#!/usr/bin/env python3

import sys
from util import Grid, E, S, W
from functools import cache

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

g = Grid(xs)

ps = g.points_by_value()["S"]

@cache
def foo(p):
    np = p + S
    v = g.d.get(np)

    if v is None:
        return 1
    elif v == "^":
        return foo(np + W) + foo(np + E)
    else:
        return foo(np)

print(foo(ps[0]))
