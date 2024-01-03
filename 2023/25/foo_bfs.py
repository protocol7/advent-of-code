import sys
from collections import defaultdict, Counter, deque
from math import prod
from util import bfs
import random

def parse(line):
    a, b = line.strip().split(": ")
    return a, b.split()

xs = list(map(parse, sys.stdin))

graph = defaultdict(set)

for a, bs in xs:
    for b in bs:
        graph[a].add(b)
        graph[b].add(a)

keys = list(graph.keys())

# try to bfs the graph. the minimal cuts are likely to be traversed more often
c = Counter()
for _ in range(1000):
    start = random.choice(keys)
    end = random.choice(keys)

    if start == end:
        continue

    path = bfs(graph, start, end)

    for edge in zip(path, path[1:]):
        edge = tuple(sorted(edge))
        c[edge] += 1

# we have now likely found the edge to cut
cut = [edge for edge, _ in c.most_common(3)]

# cut them
for a, b in cut:
    graph[a].remove(b)
    graph[b].remove(a)

# flood fill to count the connected components
def count_connected(graph, start):
    q = deque([start])
    seen = set()

    while q:
        a = q.popleft()

        if a in seen:
            continue
        seen.add(a)

        for b in graph[a]:
            q.append(b)

    return len(seen)

a, b = cut[0]
na = count_connected(graph, a)
nb = count_connected(graph, b)
print(na * nb)
