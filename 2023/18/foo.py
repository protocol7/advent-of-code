import sys
from util import Grid, Point, RIGHT, LEFT, DOWN, UP


def parse(line):
    a, b, c = line.strip().split()
    b = int(b)

    return a, b


xs = list(map(parse, sys.stdin))

ps = set()
p = Point(0, 0)

ds = {
    "R": RIGHT,
    "L": LEFT,
    "D": DOWN,
    "U": UP,
}

for d, l in xs:
    d = ds[d]

    for i in range(l):
        p += d
        ps.add(p)

g = Grid(ps)

p = Point(1, 1)

def boundary(p):
    return g[p]

g.flood_fill(p, boundary, True)

print(len(g.points_by_value()[True]))
