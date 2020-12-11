import sys
from collections import *
from itertools import *
from util import *

def parse(line):
    return line.strip()

xs = tuple(map(parse, sys.stdin))
d = grid_to_dict(xs)

seen = set()

while True:
    dd = frozenset(d.items())
    if dd in seen:
        print(list(d.values()).count("#"))
        break
    seen.add(dd)

    dn = dict()

    for x in range(len(xs[0])):
        for y in range(len(xs)):
            c = d[(x, y)]

            cc = 0
            for dx, dy in adjacent:
                for l in count(1):
                    xx = x + dx * l
                    yy = y + dy * l

                    g = d.get((xx, yy))

                    if g is None:
                        break
                    elif g == "#":
                        cc += 1
                        break
                    elif g == "L":
                        break

            nc = c
            if c == "L" and cc == 0:
                nc = "#"
            elif c == "#" and cc >= 5:
                nc = "L"
            dn[(x, y)] = nc

    d = dn