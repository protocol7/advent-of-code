#!/usr/bin/env python3

import sys
from collections import *
from itertools import *
from util import *

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

g = Grid(xs)

start = g.points_by_value()["S"][0]
end = g.points_by_value()["E"][0]

g.d[start] = '.'
g.d[end] = '.'

# Dijkstra's shortest path for a weighted graph
# graph is a dict of node -> dict of neighbour and weight
# start is the starting node
# end is the target node, or a predicate function
# returns tuple of best path and total weight
def dijkstra(graph, start, dir, end):
    best = defaultdict(lambda: maxsize)

    q = [(0, [(start, dir)])]

    while q:
        cost, path = heappop(q)
        node, dir = path[-1]

        if node == end:
            yield path, cost

        for neighbour, ndir, neighbour_cost in graph(node, dir):
            nc = cost + neighbour_cost

            if nc <= best[(neighbour, ndir)]:
                best[(neighbour, ndir)] = nc

                heappush(q, (nc, path + [(neighbour, ndir)]))

def graph(p, dir):
    ldir = turn_left(dir)
    rdir = turn_right(dir)

    for ndir, cost in [(dir, 1), (ldir, 1001), (rdir, 1001)]:
        np = p + ndir
        nv = g[np]

        if nv == '.':
            yield np, ndir, cost

seen = set()
lowest = sys.maxsize
for path, cost in dijkstra(graph, start, RIGHT, end):
    if cost <= lowest:
        seen.update(p for p, _ in path)
        lowest = cost
    else:
        break

print(len(seen))

