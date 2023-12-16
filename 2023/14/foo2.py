import sys
from itertools import count
from util import Point, UP, DOWN, LEFT, RIGHT


def parse(line):
    return line.strip()


xs = list(map(parse, sys.stdin))

w = len(xs[0])
h = len(xs)
os = set()
cs = set()

for y, row in enumerate(xs):
    for x, c in enumerate(row):
        if c == "#":
            cs.add(Point(x, y))
        elif c == "O":
            os.add(Point(x, y))


def ray(os, cs, point, direction):
    p = point + direction
    out = point
    while p.x >= 0 and p.y >= 0 and p.x < w and p.y < h and p not in cs and p not in os:
        out = p
        p += direction

    return out


def tilt(os, cs, dir):
    rev = dir == DOWN or dir == RIGHT

    for o in sorted(os, reverse=rev):
        no = ray(os, cs, o, dir)
        os.remove(o)
        os.add(no)

    return os


def turn(os, cs):
    # north, then west, then south, then east
    for d in (UP, LEFT, DOWN, RIGHT):
        os = tilt(os, cs, d)

    return os


seen = {frozenset(os): 0}

ts = 1000000000 - 1

for i in count():
    os = turn(os, cs)

    d = frozenset(os)

    if d in seen:
        break

    seen[d] = i

# get the cycle length
d = i - seen[d]

# jump head
i += int((ts - i) / d) * d

for _ in range(ts - i):
    os = turn(os, cs)

print(sum(h - y for _, y in os))
