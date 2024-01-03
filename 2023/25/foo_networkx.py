import sys
from collections import defaultdict
from math import prod
from networkx import Graph, minimum_edge_cut, connected_components

def parse(line):
    a, b = line.strip().split(": ")
    return a, b.split()


xs = list(map(parse, sys.stdin))

graph = defaultdict(set)

for a, bs in xs:
    for b in bs:
        graph[a].add(b)
        graph[b].add(a)

g = Graph()
for n in graph.keys():
    g.add_node(n)

seen = set()
for a, bs in graph.items():
    for b in bs:
        if (a, b) in seen:
            continue
        seen.add((b, a))
        g.add_edge(a, b)

cut = minimum_edge_cut(g)

for a, b in cut:
    g.remove_edge(a, b)

print(prod(map(len, connected_components(g))))
