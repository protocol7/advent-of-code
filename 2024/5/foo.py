#!/usr/bin/env python3

import sys
from collections import defaultdict
from util import ints

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
    valid = True

    for i in range(len(xx)):
        prefix = set(xx[:i])
        number = xx[i]
        forbidden = rules.get(number, set())

        if forbidden & prefix:
            valid = False
            break

    if valid:
        mid = len(xx) // 2

        t += xx[mid]

print(t)
