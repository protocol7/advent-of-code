import sys
from util import *
from functools import cache

def parse(line):
    return ints(line.strip())

xs = list(map(parse, sys.stdin))

d = {}
for y in range(len(xs)):
    for x in range(len(xs[0])):
        d[(x, y)] = xs[y][x]

@cache
def foo(a, ns, b):
    if not ns:
        return d[(a, b)]
    elif len(ns) == 1:
        return d[(a, ns[0])] + d[(ns[0], b)]
    else:
        s = sys.maxsize
        for n in ns:
            nns = tuple(x for x in ns if x != n)

            s = min(s, foo(a, nns, n) + d[(n, b)])

        return s

print(foo(0, tuple(range(1, len(xs))), 0))
