#!/usr/bin/env python3

import sys
from util import flatten, topo_sort
from random import randrange

def parse(line):
    return line.strip().split()

a, b = sys.stdin.read().strip().split("\n\n")

a = list(map(parse, a.split("\n")))
b = list(map(parse, b.split("\n")))

wires = {k[0:-1]: v == "1" for k, v in a}

gates = {w3: (w1, g, w2) for w1, g, w2, _, w3 in b}

def to_int(wires, prefix):
    zwires = {w:b for w, b in wires.items() if w[0] == prefix}

    s = ""
    for w, b in sorted(zwires.items(), reverse=True):
        s += str(int(b))

    return int(s, 2)

def to_graph(gates):
    graph = {}
    for w3, (w1, g, w2) in gates.items():
        graph[w3] = (w1, w2)

    return graph

def print_dot(gates):
    print("digraph {")
    for k, (a, g, b) in gates.items():
        color = "black"
        if g == "AND":
            color = "red"
        elif g == "OR":
            color = "blue"
        print(f"{k} -> {a} [color=\"{color}\"];")
        print(f"{k} -> {b} [color=\"{color}\"];")

    print("}")


def run(gates, wires):
    wires = wires.copy()

    graph = to_graph(gates)

    def compute(w1, g, w2):
        if g == "AND":
            return wires[w1] & wires[w2]
        elif g == "OR":
            return wires[w1] | wires[w2]
        elif g == "XOR":
            return wires[w1] ^ wires[w2]

    zwires = [w for w in graph if w[0] == "z"]
    for z in zwires:
        p = topo_sort(graph, z)

        p = p[::-1]

        for w in p:
            if w in wires:
                continue

            w1, g, w2 = gates[w]

            wires[w] = compute(w1, g, w2)

    return to_int(wires, "z")

def validate(gates, wires):
    wires = wires.copy()

    for _ in range(100):
        rx = randrange(2**45)
        ry = randrange(2**45)

        rz = rx + ry

        bx = bin(rx)[2:]
        by = bin(ry)[2:]
        expected_bz = bin(rz)[2:]

        # reset wires
        for k, v in wires.items():
            wires[k] = False

        for i, x in enumerate(bx[::-1]):
            wires["x" + str(i).rjust(2, "0")] = x == "1"
        for i, y in enumerate(by[::-1]):
            wires["y" + str(i).rjust(2, "0")] = y == "1"

        z = run(gates, wires)
        actual_bz = bin(z)[2:]

        for i, (eb, ab) in enumerate(zip(expected_bz[::-1], actual_bz[::-1])):
            if eb != ab:
                print(f"invalid at z{i}")
                return False

    return True

# swaps as determined by looking for z wires with non-XOR gates (as a half-adder must have), and by starring at the dot graph
swaps = [
    ("z07", "bjm"),
    ("z13", "hsw"),
    ("z18", "skf"),
    ("wkr", "nvr"),
]

for g1, g2 in swaps:
    gates[g1], gates[g2] = gates[g2], gates[g1]

if validate(gates, wires):
    print(",".join(sorted(flatten(swaps))))
