#!/usr/bin/env python3

import sys
from util import ints

def parse(line):
    return ints(line.strip())

xs = list(map(parse, sys.stdin))

a = sorted(x[0] for x in xs)
b = sorted(x[1] for x in xs)

print(sum(abs(x - y) for x, y in zip(a, b)))

print(sum(x * b.count(x) for x in a))
