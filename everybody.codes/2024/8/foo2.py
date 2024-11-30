#!/usr/bin/env python3

import sys
from itertools import count

priests = int(sys.stdin.read().strip())
acolytes = 1111
supply = 20240000

s = 0
total_thickness = 1
thickness = 1
for l in count(1):
    if l == 1:
        s += l
    else:
        thickness = (thickness * priests) % acolytes

        total_thickness += thickness

        p = (l - 1) * thickness * 2 + thickness

        s += p

        if s >= supply:
            base = l * 2 - 1
            order = s - supply
            print(base * order)
            break



