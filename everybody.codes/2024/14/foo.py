#!/usr/bin/env python3

import sys
from collections import *
from itertools import *
from util import *

xs = sys.stdin.read().strip().split(",")

p = Point(0, 0)
mh = 0
for x in xs:
    d = x[0]
    n = int(x[1:])

    if d == "R":
        p = p + (n, 0)
    elif d == "L":
        p = p + (-n, 0)
    elif d == "U":
        p = p + (0, n)
    elif d == "D":
        p = p + (0, -n)
    elif d == "F":
        pass
    elif d == "B":
        pass
    else:
        assert False, d

    mh = max(mh, p.y)

print(mh)
