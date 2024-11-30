#!/usr/bin/env python3

import sys
from collections import Counter

def parse(line):
    a, b = line.strip().split(":")

    return a, b.split(",")

xs = {k: v for k, v in map(parse, sys.stdin)}

print(xs)

c = Counter("Z")

for _ in range(10):
    nc = Counter()

    for k, v in c.items():
        for nk in xs[k]:
            nc[nk] += v

    c = nc

print(sum(c.values()))
