#!/usr/bin/env python3

import sys
from collections import *
from itertools import *
from util import *
from functools import *


def parse(line):
    return line.strip()


xs = list(map(parse, sys.stdin))

g = Grid(xs)

@cache
# return how many meters we can gain from here
def rec(p, dir, remaining_sec):
    if remaining_sec == 0:
        return 0

    dirs = [dir, turn_left(dir), turn_right(dir)]

    ma = -1
    for ndir in dirs:
        np = p + ndir
        v = g[np]
        if v == '#' or v == None:
            continue

        if v == "." or v == "S":
            gain = -1
        elif v == "+":
            gain = 1
        elif v == "-":
            gain = -2
        else:
            assert False

        ma = max(ma, gain + rec(np, ndir, remaining_sec - 1))

    return ma

start = g.points_by_value()["S"][0]

print(rec(start, DOWN, 100))
