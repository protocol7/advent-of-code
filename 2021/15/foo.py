import sys
from collections import *
from util import *

def parse(line):
    return list(map(int, line.strip()))

g = list(map(parse, sys.stdin))

def expand(g):
    gg = []

    for cy in range(len(g) * 5):
        dg = []

        for cx in range(5):
            for c in g[cy % len(g)]:
                cc = c + cx + cy // len(g)

                if cc > 9:
                    cc = cc % 9

                dg.append(cc)

        gg.append(dg)

    return gg

def grid_to_distances(g):
    distances = defaultdict(dict)

    for x, y, _ in iter_grid(g):
        for xx, yy in iter_orthogonal(x, y, g):
            c = g[yy][xx]

            distances[(x, y)][(xx, yy)] = c

    return distances

def run(g):
    distances = grid_to_distances(g)

    end = max(distances.keys())

    _, c = dijkstra(distances, (0, 0), end)

    return c

print(run(g))
print(run(expand(g)))