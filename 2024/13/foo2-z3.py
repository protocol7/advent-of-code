#!/usr/bin/env python3

import sys
from util import ints
from z3 import Solver, Int, sat

def parse(x):
    x = x.split("\n")
    a, aa = ints(x[0])
    b, bb = ints(x[1])
    c, cc = ints(x[2])

    c += 10000000000000
    cc += 10000000000000

    return (a, aa), (b, bb), (c, cc)

xs = sys.stdin.read().strip().split("\n\n")
cs = [parse(x) for x in xs]

t = 0
for x in cs:
    (x1, y1), (x2, y2), (x3, y3) = x

    s = Solver()
    a = Int("a")
    b = Int("b")

    s.add(a * x1 + b * x2 == x3)
    s.add(a * y1 + b * y2 == y3)

    if s.check() == sat:
        a = s.model()[a].as_long()
        b = s.model()[b].as_long()

        t += a * 3 + b

print(t)
