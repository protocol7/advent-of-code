import sys
from util import *

def parse(line):
    return list(map(int, line.strip()))

g = list(map(parse, sys.stdin))

f = 0
for _ in range(100):
    for x, y, _ in iter_grid(g):
        g[y][x] += 1

    flashed = set()
    while True:
        fl = len(flashed)

        for x, y, c in iter_grid(g):
            k = (x, y)
            if c > 9 and k not in flashed:
                flashed.add(k)

                for xx, yy in iter_adjacent(x, y, g):
                    g[yy][xx] += 1

        if len(flashed) == fl:
            break

    for x, y in flashed:
        g[y][x] = 0

    f += len(flashed)

print(f)