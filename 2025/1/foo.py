#!/usr/bin/env python3

import sys

def parse(line):
    return line[0], int(line[1:])

xs = list(map(parse, sys.stdin))

pos = 50
c = 0
for d, x in xs:
    sign = -1 if d == "L" else 1

    pos = (sign * x + pos) % 100

    c += pos == 0

print(c)
