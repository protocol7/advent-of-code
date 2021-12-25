import sys
from itertools import *
from util import *

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

d = {}
for x, y, c in iter_grid(xs):
    if c != ".":
        d[(x, y)] = c

h = len(xs)
w = len(xs[0])

for r in count(1):
    # east
    nd = {}
    for (x, y), c in d.items():
        if c == ">":
            nx = (x + 1) % w

            if (nx, y) in d:
                nd[x, y] = c
            else:
                nd[nx, y] = c

    # south    
    for (x, y), c in d.items():
        if c == "v":
            ny = (y + 1) % h

            if (x, ny) in d and d[(x, ny)] == "v" or (x, ny) in nd:
                nd[x, y] = c
            else:
                nd[x, ny] = c

    if d == nd:
        print(r)
        break

    d = nd