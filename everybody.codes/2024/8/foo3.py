#!/usr/bin/env python3

import sys
from itertools import count

priests = int(sys.stdin.read().strip())
acolytes = 10
supply = 202400000

thickness = 1
columns = []
for l in count(1):
    if l == 1:
        columns.append(l)
    else:
        thickness = (thickness * priests) % acolytes + acolytes

        columns = [c + thickness for c in columns]
        columns.insert(0, thickness)
        columns.append(thickness)

        w = len(columns)
        r = 0
        for c in columns[1:-1]:
            r += (priests * w * c) % acolytes

        s = sum(columns) - r

        if s >= supply:
            order = s - supply
            print(order)
            break



