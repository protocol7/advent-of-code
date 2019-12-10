import sys
from itertools import *
from collections import *
from fractions import gcd
from math import atan2, pi
from util import *
from heapq import heappush, heappop

def parse(line):
    return line.strip()

parsed = map(parse, sys.stdin)

m = set()
for y, line in enumerate(parsed):
    for x, c in enumerate(line):
        if c == "#":
            m.add((x, y))

# find the best astroid
ss = []
for x, y in m:
    seen = set()
    for xx, yy in m:
        if x == xx and y == yy:
            continue
        dx = xx - x
        dy = yy - y
        g = abs(gcd(dx, dy))
        dx /= g
        dy /= g

        seen.add((dx, dy))

    ss.append((len(seen), x, y))

ast = max(ss, key=lambda x: x[0])
ax, ay = ast[1:]

# bucket all astroids based on direction from best astroid. Order by distance
d = defaultdict(list)
for x, y in m:
    if x == ax and y == ay:
        continue
    dx = ax - x
    dy = ay - y
    g = abs(gcd(dx, dy))
    dx /= g
    dy /= g
    # put items on list in distance order
    dist = manhattan((x, y), (ax, ay))
    heappush(d[(dx, dy)], (dist, (x, y)))

def at(p):
    x, y = p
    a = atan2(x, -y)
    if a == pi:
        a = 0
    return a

# sort astroids by angle from best astroid
keys = sorted(d.keys(), key=at)

# go around nuking until the 200th
nuked = 0
for r in cycle(keys):
    v = d[r]
    if v:
        _, (px, py) = heappop(v)
        nuked += 1
        if nuked == 200:
            print(px * 100 + py)
            break
