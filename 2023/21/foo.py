import sys
from util import Grid

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

g = Grid(xs)

start = g.points_by_value()["S"][0]

g.d[start] = "."

pos = set([start])
for _ in range(64):
    npos = set()

    for p in pos:
        for np, nv in g.orthogonal(p):
            if nv is None or nv == "#":
                continue

            npos.add(np)

    pos = npos

print(len(pos))
