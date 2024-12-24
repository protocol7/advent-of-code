#!/usr/bin/env python3

import sys
from util import topo_sort

def parse(line):
    return line.strip().split()

a, b = sys.stdin.read().strip().split("\n\n")

a = list(map(parse, a.split("\n")))
b = list(map(parse, b.split("\n")))

wires = {k[0:-1]: v == "1" for k, v in a}

gates = {w3: (w1, g, w2) for w1, g, w2, _, w3 in b}
graph = {w3: (w1, w2) for w1, g, w2, _, w3 in b}

zwires = [w for w in graph if w[0] == "z"]

def compute(w1, g, w2):
    if g == "AND":
        return wires[w1] & wires[w2]
    elif g == "OR":
        return wires[w1] | wires[w2]
    elif g == "XOR":
        return wires[w1] ^ wires[w2]


for z in zwires:
    p = topo_sort(graph, z)

    p = p[::-1]

    for w in p:
        if w in wires:
            continue

        w1, g, w2 = gates[w]

        wires[w] = compute(w1, g, w2)

zwires = {w:b for w, b in wires.items() if w[0] == "z"}

s = "".join(str(int(b)) for w, b in sorted(zwires.items(), reverse=True))

print(int(s, 2))
