import sys
from util import Grid, UP


def parse(line):
    return line.strip()


xs = list(map(parse, sys.stdin))

g = Grid(xs)

os = g.points_by_value()["O"]

def ray(self, point, direction):
    p = point + direction
    out = point
    while p in self and self[p] == ".":
        out = p
        p += direction

    return out

for o in os:
    no = ray(g, o, UP)
    g[o] = "."
    g[no] = "O"
    
ROWS = g.max()[1]

print(sum(ROWS - y + 1 for _, y in g.points_by_value()["O"]))
