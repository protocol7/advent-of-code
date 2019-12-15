import sys
from collections import *
from intcode import *

prog = parse(sys.stdin)
inp = []
inp_iter = iter(inp)
ic = Intcode(prog, lambda: next(inp_iter))

# table of delta x, delta y -> direction
dirs = {
        (0, -1): 1,
        (0, 1): 2,
        (1, 0): 3,
        (-1, 0): 4,
        }
adj = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def dfs(path, seen, graph):
    x, y = path[-1]
    oxygen = None
    for dx, dy in adj:
        xx = x + dx
        yy = y + dy

        if (xx, yy) in seen:
            continue
        seen.add((xx, yy))

        d = dirs[(xx-x, yy-y)]
        inp.append(d)
        out = ic.run()

        if out == 1 or out == 2:
            # moved
            if out == 2:
                # found the oxygen
                oxygen = (xx, yy)

            graph[(xx, yy)].add((x, y))
            graph[(x, y)].add((xx, yy))

            # search next
            o = dfs(path + [(xx, yy)], seen, graph)
            oxygen = o if o else oxygen

            # backtrack
            d = dirs[(x-xx, y-yy)]
            inp.append(d)
            out = ic.run()
            assert out == 1 or out == 2

    return oxygen

path = []
path.append((0, 0))
seen = set(path)
graph = defaultdict(set)
oxygen = dfs(path, seen, graph)

# search all possible paths until we can't progress any more
def bfs_all_paths(graph, start):
    q = deque([[start]])
    paths = []
    seen = set()

    while q:
        path = q.popleft()
        v = path[-1]
        for n in graph[v]:
            if n in seen:
                continue
            seen.add(n)

            q.append(path + [n])
        else:
            paths.append(path)

    return paths

paths = bfs_all_paths(graph, oxygen)

print(max(map(len, paths)) - 1)
