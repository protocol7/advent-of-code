import sys
sys.setrecursionlimit(10000)
from collections import defaultdict, deque
from util import Grid, Point, ORTHOGONAL, LEFT, RIGHT, UP, DOWN, item
from copy import deepcopy

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

start = Point(xs[0].find("."), 0)
end = Point(xs[-1].find("."), len(xs) -1)


def to_graph(grid, start, dirs):
    q = deque([start])
    seen = set(q)
    g = defaultdict(dict)

    while q:
        p = q.popleft()
        v = grid[p]

        for n, nv in grid.neighbours(p, dirs(v)):
            if nv is not None and nv != "#":
                # with distance
                g[p][n] = 1

                if n not in seen:
                    q.append(n)
                    seen.add(n)
    return g


def compress(graph):
    graph = deepcopy(graph)

    for node in list(graph):
        ns = graph[node]
        if len(ns) == 2:
            na, nb = ns
            dist = ns[na] + ns[nb]

            graph[nb][na] = dist
            graph[nb].pop(node)

            graph[na][nb] = dist
            graph[na].pop(node)

            graph.pop(node)

    return graph


def dfs(graph, node, end, dist, seen):
    if node == end:
        return dist

    seen = seen | {node}

    m = -1
    for n, d in graph[node].items():
        if n not in seen:
            m = max(m, dfs(graph, n, end, dist + d, seen))

    return m


grid = Grid(xs)

# part 1
DIRS = {
        ".": ORTHOGONAL,
        ">": [RIGHT],
        "<": [LEFT],
        "^": [UP],
        "v": [DOWN],
    }

graph = to_graph(grid, start, lambda v: DIRS[v])
print(dfs(graph, start, end, 0, set()))

# part 2
graph = compress(to_graph(grid, start, lambda _: ORTHOGONAL))

# the end if only connected to one other node, so if we reach that, we are done
penultimate = item(graph[end])

print(dfs(graph, start, penultimate, 0, set()) + graph[end][penultimate])
