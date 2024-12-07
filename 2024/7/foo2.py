#!/usr/bin/env python3

import sys
from util import ints
from operator import mul, add

xs = list(map(ints, sys.stdin))

def concat(a, b):
    return int(str(a) + str(b))

OPS = [add, mul, concat]

def rec(rem, val, ans):
    if val > ans:
        return False
    if not rem:
        return val == ans

    return any(rec(rem[1:], op(val, rem[0]), ans) for op in OPS)

t = 0
for x in xs:
    ans = x[0]
    ps = x[1:]

    if rec(ps[1:], ps[0], ans):
        t += ans

print(t)
