import sys
from collections import *
from itertools import *
from util import *


def parse(line):
    return line.strip()


xs = list(map(parse, sys.stdin))

g = Grid(xs)


start = g.points_by_value()["S"][0]

g.d[start] = "."

#g.pretty_print()
print(start)

def pp(g, pos):
    for y, row in enumerate(g.rows()):
        s = ""
        for p, c in row:
            #p = Point(x, y)

            if p in pos:
                s += "O"
            else:
                s += c

        print(s)

pos = set([start])
for _ in range(64):
    npos = set()

    for p in pos:
        for np, nv in g.orthogonal(p):
            if nv is None:
                continue

            if nv == "#":
                continue

            npos.add(np)

    pos = npos


pp(g, pos)
print(len(pos))
