import sys
sys.setrecursionlimit(1500)

from util import *
from functools import cache

def parse(line):
    return ints(line.strip())

xs = list(map(parse, sys.stdin))

width = len(xs[0])
vac = 5

@cache
def foo(y, x):
    if y >= len(xs):
        return 0

    mc = 0
    for dx in (-1, 0, 1):
        nx = x + dx
        if nx < 0 or nx > width - vac:
            continue

        mc = max(mc, foo(y+1, nx))

    return sum(xs[y][x:x+vac]) + mc

m = 0
for x in range(width - vac + 1):
    m = max(m, foo(0, x))

print(m)