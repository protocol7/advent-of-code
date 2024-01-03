import sys
from collections import defaultdict
import random
from math import prod

def parse(line):
    a, b = line.strip().split(": ")
    return a, b.split()

xs = list(map(parse, sys.stdin))

graph = defaultdict(set)

for a, bs in xs:
    for b in bs:
        graph[a].add(b)
        graph[b].add(a)

# from https://github.com/dps/aoc/blob/main/2023/day25/kargers.py
def kargers(graph):
    while True:
        # Implementation based on https://en.wikipedia.org/wiki/Karger%27s_algorithm
        # V maps node name to a list of nodes connected via edges (incl. repeats!) and a set
        # of the original nodes which have been merged in to n.
        V = {n: (list(v), set([n])) for n, v in graph.items()}

        # run until we've partitioned the graph into two
        while len(V.keys()) > 2:
            start = random.choice(list(V.keys()))
            start_neigh = random.choice(V[start][0])

            start_edges, start_neigh_edges = V[start], V[start_neigh]

            # for all edges in starts neighbour, move those edges directly to the start node, and remove start_neigh from the graph
            for edge in start_neigh_edges[0]:
                if edge != start:
                    # add this edge to the list of edges on the start node
                    start_edges[0].append(edge)
                    # end remove if from start_neigh
                    V[edge][0].remove(start_neigh)
                    # and add the start node to the edge
                    V[edge][0].append(start)

            V[start] = ([d for d in start_edges[0] if d != start_neigh], start_edges[1] | start_neigh_edges[1])

            del V[start_neigh]

        # try until there are exactly three cuts
        if len(list(V.values())[0][0]) == 3:
            return prod(len(v[1]) for v in V.values())

print(kargers(graph))
