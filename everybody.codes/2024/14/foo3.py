#!/usr/bin/env python3

import sys
from collections import *
from itertools import *
from util import *
from dataclasses import dataclass

def parse(line):
    return line.strip().split(",")

xs = list(map(parse, sys.stdin))

@dataclass
class Point3D:
    x: int
    y: int
    z: int

    def __add__(self, other):
        return Point3D(self.x + other[0], self.y + other[1], self.z + other[2])

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"

leafs = set()
seen = set()
for xx in xs:
    p = Point3D(0, 0, 0)
    leaf = p
    for x in xx:
        d = x[0]
        n = int(x[1:])

        if d == "R":
            dir = (1, 0, 0)
        elif d == "L":
            dir = (-1, 0, 0)
        elif d == "U":
            dir = (0, 1, 0)
        elif d == "D":
            dir = (0, -1, 0)
        elif d == "F":
            dir = (0, 0, 1)
        elif d == "B":
            dir = (0, 0, -1)
        else:
            assert False, d

        for _ in range(n):
            p = p + dir

            seen.add(p)

        leaf = p

    leafs.add(leaf)


dirs = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
graph = {}
for p in seen:
    ns = []
    for dir in dirs:
        np = p + dir
        if np in seen:
            ns.append(np)
    graph[p] = ns

min_y = min(p.y for p in leafs)
max_y = max(p.y for p in leafs)
min_murkiness = sys.maxsize

for y in range(min_y, max_y+1):
    murkiness = 0
    failed = False
    for leaf in leafs:
        path = bfs(graph, leaf, lambda p: p.x == 0 and p.y == y and p.z == 0)

        if path is None:
            failed = True
            break
        else:
            murkiness += len(path) - 1

    if not failed:
        min_murkiness = min(min_murkiness, murkiness)

print(min_murkiness)
