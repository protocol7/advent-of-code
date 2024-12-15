#!/usr/bin/env python3

import sys
from util import ints
from math import prod

def parse(line):
    return ints(line.strip())

xs = list(map(parse, sys.stdin))

w = 101
h = 103

rounds = 100

midx = w // 2
midy = h // 2

qs = [0, 0, 0, 0]
for x, y, vx, vy in xs:
    x = (x + rounds * vx) % w
    y = (y + rounds * vy) % h

    if x < midx and y < midy:
        qs[0] += 1
    elif x > midx and y < midy:
        qs[1] += 1
    elif x < midx and y > midy:
        qs[2] += 1
    elif x > midx and y > midy:
        qs[3] += 1

print(prod(qs))
