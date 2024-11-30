#!/usr/bin/env python3

import sys
from collections import *
from itertools import *
from util import *


def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

g = Grid(xs)

starts = g.points_by_value()["S"]
end = g.points_by_value()["E"][0]

def to_graph(grid, start, is_neighbour, neighbours=ORTHOGONAL):
    if type(start) == list:
        q = [Point(s) for s in start]
    else:
        q = [Point(start)]

    seen = set(q)
    g = defaultdict(list)

    while q:
        p = heappop(q)

        for n, _ in grid.neighbours(p, neighbours):
            if is_neighbour(p, grid[p], n, grid[n]):
                vp = int(grid[p]) if grid[p].isdigit() else 0
                vn = int(grid[n]) if grid[n].isdigit() else 0

                d = min(abs(vp - vn), 10 - abs(vp - vn))

                g[p].append((n, d + 1))

                if n not in seen:
                    heappush(q, n)
                    seen.add(n)
    return g


def is_neighbour(_, __, ___, v):
    return v and (v.isdigit() or v in "SE")

graph = to_graph(g, end, is_neighbour)

# Dijkstra's shortest path for a weighted graph
# graph is a dict of node -> dict of neighbour and weight
# start is the starting node
# end is the target node, or a predicate function
# returns tuple of best path and total weight
def dijkstra(graph, start, end):
    best = defaultdict(lambda: maxsize)
    q = [(0, [start])]

    if callable(end):
        end_fn = end
    else:
        end_fn = lambda x: x == end

    while q:
        cost, path = heappop(q)
        node = path[-1]

        if end_fn(node):
            return path, cost

        for neighbour, neighbour_cost in graph[node]:
            nc = cost + neighbour_cost

            if nc < best[neighbour]:
                best[neighbour] = nc

                heappush(q, (nc, path + [neighbour]))

_, cost = dijkstra(graph, end, lambda node: g[node] == "S")

print(cost)
