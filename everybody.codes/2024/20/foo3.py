#!/usr/bin/env python3

import sys
sys.setrecursionlimit(10000)
from collections import *
from itertools import *
from util import *
from functools import *
from heapq import *


def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

g = Grid(xs)

start = g.points_by_value()["S"][0]

# looking at the input, moving 2 steps to the right, and then glide straight down is the best strategy

start.x += 2

path = [row[start.x] for row in g.rows()]

def run():
    alt = 384400 - 1
    for i, v in enumerate(cycle(path)):
        if v == ".":
            alt -= 1
        elif v == "+":
            alt += 1

        if alt == 0:
            return i

print(run())

