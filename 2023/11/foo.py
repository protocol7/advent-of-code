import sys
from itertools import product
from util import Grid, diffrange, transpose, manhattan


def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

e_rows = {i for i, row in enumerate(xs) if all(c == "." for c in row)}
e_cols = {i for i, row in enumerate(transpose(xs)) if all(c == "." for c in row)}

g = Grid(xs)
galaxies = g.points_by_value()["#"]

for expansion in [2, 1000000]:
    dist = 0

    for g1, g2 in product(galaxies, repeat=2):
        cols = set(diffrange(g1.x, g2.x))
        rows = set(diffrange(g1.y, g2.y))

        dist += manhattan(g1, g2)

        dist += len(cols & e_cols) * (expansion - 1)
        dist += len(rows & e_rows) * (expansion - 1)

    print(dist // 2)
