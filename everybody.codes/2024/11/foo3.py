#!/usr/bin/env python3

import sys
from collections import Counter

def parse(line):
    a, b = line.strip().split(":")

    return a, b.split(",")

xs = {k: v for k, v in map(parse, sys.stdin)}

def grow(start):
    c = Counter([start])

    for _ in range(20):
        nc = Counter()

        for k, v in c.items():
            for nk in xs[k]:
                nc[nk] += v

        c = nc

    return sum(c.values())

vals = []
for start in xs:
    vals.append(grow(start))

print(max(vals) - min(vals))
