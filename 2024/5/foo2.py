#!/usr/bin/env python3

import sys
from collections import defaultdict
from util import ints, topo_sort

def parse(line):
    return ints(line.strip())

a, b = sys.stdin.read().split("\n\n")
a = a.strip().split("\n")
b = b.strip().split("\n")

rules = defaultdict(set)
for x, y in map(parse, a):
    rules[x].add(y)

t = 0
for xx in map(parse, b):
    rr = {x: rules.get(x, set()) & set(xx) for x in xx}

    for x in xx:
        ts = topo_sort(rr, x)
        if len(ts) == len(xx) and ts != xx:
            mid = len(xx) // 2
            t += ts[mid]

print(t)
