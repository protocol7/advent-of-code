import sys
from collections import *
from util import *

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

d = defaultdict(bool)

for line in xs:
    x, y, z = 0, 0, 0

    dir = ""
    for c in line:
        if c in "sn":
            dir = c
            continue
        elif c in "we":
            dir += c

        dx, dy, dz = hex_adjacent_ew[dir]
        x += dx
        y += dy
        z += dz

        dir = ""

    k = (x, y , z)
    d[k] = not d[k]

def count(d):
    return sum(v for v in d.values())

def new_value(d, x, y, z):
    c = sum(d[(x+dx, y+dy, z+dz)] for dx, dy, dz in hex_adjacent_ew.values())

    if d[(x, y, z)]:
        return 0 < c < 3
    else:
        return c == 2

for turn in range(100):

    nd = defaultdict(bool)

    for x, y, z in set(d.keys()):
        # check current + adjacent
        for dx, dy, dz in [(0, 0, 0)] + list(hex_adjacent_ew.values()):
            xx = x + dx
            yy = y + dy
            zz = z + dz
            if new_value(d, xx, yy, zz):
                nd[(xx, yy, zz)] = True

    d = nd

    print(turn+1, count(d))

print(count(d))