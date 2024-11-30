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

for _ in range(100):
    for rot, p in zip(cycle(a), rot_points()):
        if rot == 'L':
            rotate(g, p, True)
        elif rot == 'R':
            rotate(g, p, False)
        else:
            assert False

g.pretty_print()
