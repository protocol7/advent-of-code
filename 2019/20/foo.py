import sys
from collections import *
from util import *

t = list(map(lambda s: s.strip("\n"), sys.stdin))

adj = [(0, -1), (0, 1), (-1, 0), (1, 0)]
m = []
labels = dict()
for y in range(2, len(t) - 2):
    line = []
    for x in range(2, len(t[0]) - 2):
        c = t[y][x]
        if c == ".":
            for ax, ay in adj:
                lx = x + ax
                ly = y + ay
                l = t[y+ay][x+ax] + t[y+2*ay][x+2*ax]
                if l.isalpha():
                    if ax < 0 or ay < 0:
                        l = l[::-1]
                    labels[(x-2, y-2)] = l

        if c in ("#", "."):
            line.append(c)
        else:
            line.append("#")
    m.append(line)

ps = defaultdict(list)
for c, l in labels.items():
    ps[l].append(c)

portals = dict()
for l, cs in ps.items():
    if len(cs) == 2:
        c1, c2 = cs
        portals[c1] = c2
        portals[c2] = c1
    else:
        if l == "AA":
            start = cs[0]
        elif l == "ZZ":
            goal = cs[0]

def maze_to_graph(maze, start, labels):
    q = [start]
    seen = set([start])
    g = defaultdict(list)
    w = len(maze[0])
    h = len(maze)

    while q:
        c = heappop(q)
        cx, cy = c

        for dx, dy in adj:
            n = cx + dx, cy + dy
            nx, ny = n

            if nx < 0 or ny < 0 or nx >= w or ny >= h:
                continue

            if m[ny][nx] == ".":
                g[c].append(n)

                if n not in seen:
                    heappush(q, n)
                    seen.add(n)

        # also portal with label
        if c in portals:
            n = portals[c]
            g[c].append(n)
            if n not in seen:
                heappush(q, n)
                seen.add(n)

    return g

g = maze_to_graph(m, start, labels)

p = bfs(g, start, lambda c: c == goal)
print(len(p) - 1)
