import sys
from collections import *
from itertools import *
from util import *
from heapq import heappop, heappush


# graph if a function of node -> nodes and distances
def bfs(graph, start, goal):
    q = [(0, [start])]
    seen = set()

    while q:
        cost, path = heappop(q)
        c = path[-1]

        if c in seen:
            continue
        seen.add(c)

        if c == goal:
            return cost, path

        for n, dist in graph(c):
                priority = cost + dist
                heappush(q, (priority, path + [n]))

m = []
bots = dict()
keys = dict()

for y, line in enumerate(sys.stdin):
    row = []
    line = line.strip()
    for x, c in enumerate(line):
        if c == "@":
            bots[str(len(bots))] = (x, y)
        elif c.islower():
            keys[c] = (x, y)
        row.append(c)
    m.append(row)

def isn(a, b, c, d):
    return d != "#"

paths = defaultdict(dict)
for bot, pos in bots.items():
    g = maze_to_graph(m, pos, isn)

    # precompute distances between all keys
    keys_and_start = dict(keys, **{bot:pos})
    for a, b in combinations(keys_and_start.keys(), 2):
        ap = keys_and_start[a]
        bp = keys_and_start[b]
        x = bfs(lambda n: [(x, 1) for x in g[n]], ap, bp)
        if not x:
            continue

        _, p = x

        # what keys do we need on the way?
        doors = set()
        for x, y in p[1:-1]:
            c = m[y][x]
            if c.isupper():
                doors.add(c.lower())
        paths[a][b] = (len(p) - 1, doors)
        paths[b][a] = (len(p) - 1, doors)

all_keys = set(keys)

# marker node for when we've found all keys, this will be what we're looking
# for
goal = (None, None)

# provide a list of neighbouring nodes and distances given a node
def nodes(n):
    bs, visited = n

    # are we done?
    if all_keys.issubset(visited):
        return [(goal, 0)]

    ns = []
    # for each bot
    for b in range(4):
        bot = bs[b]
        for other, (dist, required) in paths.get(bot, dict()).items():
            # have we already visitied this key?
            if other in visited:
                continue

            # do we have keys to all doors to visit the key?
            if not required.issubset(visited):
                continue

            nk = frozenset(visited | set([other]))
            nb = list(bs)
            nb[b] = other
            nb = tuple(nb)

            ns.append(((nb, nk), dist))
    return ns

cost, _ = bfs(nodes, (tuple(["0", "1", "2", "3"]), frozenset(["0", "1", "2", "3"])), goal)

print(cost)
