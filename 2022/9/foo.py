import sys
from util import *

def parse(line):
    a, b = line.strip().split()
    b = int(b)
    return a, b

xs = list(map(parse, sys.stdin))

hx, hy = (0, 0)
tx, ty = (0, 0)

dirs = {
    "U": (0, 1),
    "D": (0, -1),
    "R": (1, 0),
    "L": (-1, 0),
}

seen = set()
for a, b in xs:
    for _ in range(b):
        mx, my = dirs[a]
        hx += mx
        hy += my

        dx = hx - tx
        dy = hy - ty

        if abs(dx) > 1 or abs(dy) > 1:
            tx += sign(dx)
            ty += sign(dy)

        seen.add((tx, ty))

print(len(seen))
