#!/usr/bin/env python3

import sys
from collections import *
from itertools import *
from util import *


def parse(line):
    return line.strip()

a, b = sys.stdin.read().split('\n\n')

xs = list(map(parse, b.split('\n')))

g = Grid(xs)

def rot_points():
    for y in range(1, len(xs)-1):
        for x in range(1, len(xs[0])-1):
            yield (x, y)

def rotate(g, p, left):
    nvs = []
    for n, nv in g.adjacent(p):
        nvs.append(nv)

    if left:
        nvs = nvs[1:] + nvs[:1]
    else:
        nvs = nvs[-1:] + nvs[:-1]

    for nv, (n, _) in zip(nvs, g.adjacent(p)):
        g.d[n] = nv

# find cycles

ps = []

for y in range(len(xs)):
    row = []
    for x in range(len(xs[0])):
        row.append((x, y))
    ps.append(row)

gg = Grid(ps)


# do one round of rotations to build a map
for rot, p in zip(cycle(a), rot_points()):
    if rot == 'L':
        rotate(gg, p, True)
    elif rot == 'R':
        rotate(gg, p, False)
    else:
        assert False
print("Map built")

rot_map = {}
for p, op in gg.points():
    rot_map[op] = p

print("Finding cycles")
# find cycles
cycles = {}
for y in range(len(xs)):
    print(y / len(xs))
    for x in range(len(xs[0])):
        p = Point(x, y)
        cycle = []
        seen = set()
        while p not in seen:
            cycle.append(p)
            seen.add(p)
            p = rot_map[p]
        cycles[p] = cycle

out = {}

rounds = 1048576000

for p, v in g.points():
    cycle = cycles[p]

    np = cycle[rounds % len(cycle)]
    out[np] = v

gt = Grid(out)

gt.pretty_print()
