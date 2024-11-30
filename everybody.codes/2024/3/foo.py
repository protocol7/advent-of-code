#!/usr/bin/env python3

import sys
from util import Grid


def parse(line):
    return line.strip()

def count(g):
    return sum(v == "#" for _, v in g.points())

xs = list(map(parse, sys.stdin))

g = Grid(xs)

s = count(g)
while True:
    ng = Grid(g.d.copy())
    for p, v in g.points():
        #print(p, v)
        #print("".join(nv if nv else " " for _, nv in g.orthogonal(p)))

        if v == ".":
            continue

        if not all(nv == "#" for _, nv in g.orthogonal(p)):
            ng.d[p] = "."

    c = count(ng)

    s += c

    if c == 0:
        break

    g = ng

print(s)
