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

print(sum(v for v in d.values()))