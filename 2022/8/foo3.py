import sys
from util import *

def parse(line):
    return list(map(int, line.strip()))

xs = list(map(parse, sys.stdin))

g = Grid(xs)

seen = set()
msc = -1
for p, h in g:
    sc = 1
    for dir in ORTHOGONAL:  
        trees = [hh for _, hh in g.direction(p, dir)]

        if not trees or h > max(trees):
            seen.add(p)

        sc *= len(takeuntil(lambda x: x >= h, trees))

    msc = max(msc, sc)

print(len(seen))
print(msc)
