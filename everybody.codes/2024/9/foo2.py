#!/usr/bin/env python3

import sys
from collections import *
from itertools import *
from util import *
from functools import cache


def parse(line):
    return int(line.strip())

xs = list(map(parse, sys.stdin))

stamps = sorted([1, 3, 5, 10, 15, 16, 20, 24, 25, 30], reverse=True)

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

print(sum(rec(x) for x in xs))
