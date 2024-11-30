#!/usr/bin/env python3

import sys
from itertools import count

xs = int(sys.stdin.read().strip())

s = 0
for b in count(1, 2):
    s += b

    if s >= xs:
        print((s - xs) * b)
        break

