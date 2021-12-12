import sys
from util import *

def parse(line):
    return list(map(int, line.strip()))

g = list(map(parse, sys.stdin))

s = 0
for x, y, c in iter_grid(g):
    # if c smaller than all its neighbours?
    if all(c < g[yy][xx] for xx, yy in iter_orthogonal(x, y, g)):
        s += c + 1

print(s)
