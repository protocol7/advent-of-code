#!/usr/bin/env python3

import sys
from collections import *
from itertools import *
from util import *


def parse(line):
    return line.strip()


xs = list(map(parse, sys.stdin))

g = Grid(xs)

stars = g.points_by_value()["*"]

# The main function to construct MST using Kruskal's algorithm
# graph is a dict of node to dict of node to weight
def kruskal_minimum_spanning_tree(graph):
    # A utility function to find set of an element i
    # (truly uses path compression technique)
    def find(parent, i):
        if parent[i] != i:
            # Reassignment of node's parent
            # to root node as
            # path compression requires
            parent[i] = find(parent, parent[i])
        return parent[i]

    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(parent, rank, x, y):

        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x

        # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            parent[y] = x
            rank[x] += 1

    graph = [(u, v, w) for u, d in graph.items() for v, w in d.items()]

    # Sort all the edges in non-decreasing order of their weight
    graph = sorted(graph, key=lambda item: item[2])

    # number of unique vertices
    n_vertices = len(set(x for x, _, _ in graph) | set(x for _, x, _ in graph))

    parent = []
    rank = []

    # This will store the resultant MST
    result = []

    # Create V subsets with single elements
    parent = list(range(n_vertices))
    rank = [0] * n_vertices

    for i in count():
        # Number of edges to be taken is less than to V-1
        if len(result) >= n_vertices - 1:
            break

        # Pick the smallest edge and increment
        # the index for next iteration
        u, v, w = graph[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)

        # If including this edge doesn't
        # cause cycle, then include it in result
        # and increment the index of result
        # for next edge
        if x != y:
            result.append([u, v, w])
            union(parent, rank, x, y)
        # Else discard the edge

    return sum(w for _, _, w in result)


gg = defaultdict(dict)

for i, star in enumerate(stars):
    for j, other in enumerate(stars):
        if i != j:
            gg[i][j] = manhattan(star, other)

cost = kruskal_minimum_spanning_tree(gg)
print(cost + len(stars))
