import sys
from util import *

def parse(line):
    state = line.startswith("on")
    return state, ints(line.strip())

xs = list(map(parse, sys.stdin))

c = {}
for f in xs:
    state, (x1, x2, y1, y2, z1, z2) = f

    x1 = max(-50, x1)
    x2 = min(50, x2)

    y1 = max(-50, y1)
    y2 = min(50, y2)

    z1 = max(-50, z1)
    z2 = min(50, z2)

    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            for z in range(z1, z2+1):
                c[(x, y, z)] = state

print(sum(c.values()))