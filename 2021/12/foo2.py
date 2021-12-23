import sys
from collections import *

def parse(line):
    return line.strip().split("-")

xs = list(map(parse, sys.stdin))

# return all paths between start and end
# graph is dict of node -> neighbours
# end is predicate function
# returns list of paths from start to end
def bfs_all_paths(graph):
    q = deque([["start"]])
    paths = []

    while q:
        path = q.popleft()
        v = path[-1]
        for n in graph[v]:
            if n == "start":
                continue
            elif n.islower():
                lc = [w for w in path if w.islower()]

                if len(lc) != len(set(lc)) and n in path:
                    continue

            p = path + [n]
            if n == "end":
                paths.append(p)
            else:
                q.append(p)
    return paths

g = defaultdict(list)

for a, b in xs:
    g[a].append(b)
    g[b].append(a)
    
ps = bfs_all_paths(g)

print(len(ps))