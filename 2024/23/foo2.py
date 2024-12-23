#!/usr/bin/env python3

import sys
from collections import defaultdict

def parse(line):
    return line.strip().split("-")

xs = list(map(parse, sys.stdin))

graph = defaultdict(set)
for a, b in xs:
    graph[a].add(b)
    graph[b].add(a)


def bron_kerbosch(graph, clique, remaining, seen):
    if not remaining and not seen:
        yield clique

    while remaining:
        v = remaining.pop()
        neighbours = graph[v]

        for c in bron_kerbosch(graph, clique | {v}, remaining & neighbours, seen & neighbours):
            yield c

        seen.add(v)

all_cliques = list(bron_kerbosch(graph, set(), set(graph.keys()), set()))

print(",".join(sorted(max(all_cliques, key=len))))
