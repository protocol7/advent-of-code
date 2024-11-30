#!/usr/bin/env python3

import sys
from collections import defaultdict

def parse(line):
    p, cs = line.strip().split(":")
    return p, cs.split(",")

xs = list(map(parse, sys.stdin))

tree = {p: cs for p, cs in xs}

paths = defaultdict(list)

def rec(n, depth, path, paths):
    for c in n:
        if c == "@":
            paths[depth].append(path + [c])
            continue

        if c in tree:
            rec(tree[c], depth + 1, path + [c], paths)

rec(tree["RR"], 0, ["RR"], paths)

for k, v in paths.items():
    if len(v) == 1:
        print("".join([x[0] for x in v[0]]))
