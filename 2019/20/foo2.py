import sys
from collections import *
from heapq import heappop, heappush

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
                l = t[ly][lx]
                if l.isalpha():
                    lx = x + 2*ax
                    ly = y + 2*ay
                    l += t[ly][lx]

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

def lev(m, a, b):
    ax, ay = a
    bx, by = b

    if abs(ax-bx) < 2 and abs(ay-by) < 2:
        return 0

    if ax == 0 or ay == 0 or ax == len(m[0]) - 1 or ay == len(m) - 1:
        return -1
    elif bx == 0 or by == 0 or bx == len(m[0]) - 1 or by == len(m) - 1:
        return 1
    else:
        return 0

def rec_bfs(graph, start, end):
    q = deque([[(start, 0)]])
    seen = set()

    while q:
        path = q.popleft()
        v, level = path[-1]

        for n in graph[v]:
            # detect portal
            dl = lev(m, v, n)
            lvl = level + dl
            if lvl < 0:
                continue

            p = path + [(n, lvl)]
            if end(n, lvl):
                return p
            if (n, lvl) not in seen:
                q.append(p)
                seen.add((n, lvl))

p = rec_bfs(g, start, lambda x, l: x == goal and l == 0)
print(len(p) - 1)
