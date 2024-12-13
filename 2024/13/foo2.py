#!/usr/bin/env python3

import sys
from util import ints

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

# Wolfram Alpha to solve:
# solve(a*x1 + b*x2 = x3, a*y1 + b*y2 = y3 ,[a,b])

t = 0
for x in cs:
    (x1, y1), (x2, y2), (x3, y3) = x

    a = (x3*y2 - x2*y3) / (x1*y2 - x2*y1)
    b = (x3*y1 - x1*y3) / (x2*y1 - x1*y2)

    if a == int(a) and b == int(b):
        t += int(a * 3 + b)

print(t)
