import sys
from collections import *
from itertools import *
from util import *

def parse(line):
    return ints(line)

xs = list(map(parse, sys.stdin))

s = 0
cache = {}
for x in xs:
    rounds = x[0]
    width = x[1]
    coords = chunks(x[2:], 2)

    d = set()
    for y, x in coords:
        d.add((x, y))

    def neighbours(d, x, y):
        out = []
        for dx, dy in ORTHOGONAL:
            nx = x + dx
            ny = y + dy

            if nx < 0 or ny < 0 or nx >= width or ny >= width:
                continue

            out.append((nx, ny))

        return out

    def odd_around(d, x, y):
        on = 0
        for nx, ny in neighbours(d, x, y):
            on += (nx, ny) in d

        return on % 2 != 0

    for _ in range(rounds):
        key = frozenset(d)
        if key in cache:
            d = cache[key]
            continue

        nd = set()
        for x, y in d:
            if odd_around(d, x, y):
                nd.add((x, y))

            for nx, ny in neighbours(d, x, y):
                if odd_around(d, nx, ny):
                    nd.add((nx, ny))

        cache[key] = nd

        d = nd

    print(rounds, width, len(d))
    s += len(d)

print(s)