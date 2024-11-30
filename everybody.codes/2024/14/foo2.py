#!/usr/bin/env python3

import sys
from collections import *
from itertools import *
from util import *
from dataclasses import dataclass

def parse(line):
    return line.strip().split(",")

xs = list(map(parse, sys.stdin))

print(xs)

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


seen = set()
for xx in xs:
    print(xx)
    p = Point3D(0, 0, 0)
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

print(seen)
print(len(seen))
