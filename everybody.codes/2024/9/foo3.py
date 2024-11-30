#!/usr/bin/env python3

import sys
sys.setrecursionlimit(15000)

from collections import *
from itertools import *
from util import *
from functools import cache


def parse(line):
    return int(line.strip())

xs = list(map(parse, sys.stdin))

stamps = sorted([1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101], reverse=True)

@cache
def rec(x):
    if x == 0:
        return 0

    mi = sys.maxsize
    for s in stamps:
        if s > x:
            continue

        mi = min(mi, rec(x - s) + 1)

    return mi

s = 0
for x in xs:
    mi = sys.maxsize
    for d in range(-50, 51):
        a = x // 2 - d
        b = x // 2 + d

        # hack fix rounding error
        if a + b != x:
            b += 1

        assert a + b == x

        if abs(a - b) > 100:
            continue

        mi = min(mi, rec(a) + rec(b))

    s += mi

print(s)
