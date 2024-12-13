#!/usr/bin/env python3

import sys
from util import ints
from functools import cache

def parse(x):
    x = x.split("\n")
    a, aa = ints(x[0])
    b, bb = ints(x[1])
    c, cc = ints(x[2])

    return (a, aa), (b, bb), (c, cc)

xs = sys.stdin.read().strip().split("\n\n")
cs = [parse(x) for x in xs]

@cache
def rec(ax, ay, bx, by, dx, dy, apresses, bpresses):
    if dx < 0 or dy < 0 or apresses > 100 or bpresses > 100:
        return sys.maxsize

    if dx == 0 and dy == 0:
        return apresses * 3 + bpresses

    f = rec(ax, ay, bx, by, dx - ax, dy - ay, apresses+1, bpresses)
    g = rec(ax, ay, bx, by, dx - bx, dy - by, apresses, bpresses+1)

    return min(f, g)


t = 0
for x in cs:
    (ax, ay), (bx, by), (tx, ty) = x

    f = rec(ax, ay, bx, by, tx, ty, 0, 0)

    if f != sys.maxsize:
        t += f

print(t)
