import sys
from collections import *
from itertools import *
from util import *

def parse(line):
    return ints(line.strip())

xs = list(map(parse, sys.stdin))

xs = [(x + 3600 * dx, y + 3600 * dy, dx, dy) for x, y, dx, dy in xs]

s = set()
for _ in range(60):
    nx = []
    for x, y, dx, dy in xs:
        x += dx
        y += dy

        s.add((x, y))

        nx.append((x, y, dx, dy))

    xs = nx

d = set()
for x in range(100):
    for y in range(100):
        d.add((x, y))

d -= s

x, y = item(d)

print("%s:%s" % (x, y))