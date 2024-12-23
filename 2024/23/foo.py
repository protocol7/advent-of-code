#!/usr/bin/env python3

import sys
from collections import defaultdict, Counter
from itertools import combinations

def parse(line):
    return line.strip().split("-")

xs = list(map(parse, sys.stdin))

graph = defaultdict(set)
for a, b in xs:
    graph[a].add(b)
    graph[b].add(a)

d = Counter()
for k, v in graph.items():
    for p in combinations(v, 2):
        aa = frozenset(p + (k,))
        d[aa] += 1

mm = max(d.values())

t = 0
for k, v in d.items():
    if any(n[0] == "t" for n in k) and v == mm:
        t += 1

print(t)
