#!/usr/bin/env python3

import sys
from collections import *
from itertools import *
from util import *


def parse(line):
    return ints(line.strip())


xs = list(map(parse, sys.stdin))

xs = transpose(xs)

shout = None
for r in range(10):
    c = r % len(xs)
    n = xs[c].pop(0)

    col = xs[(c + 1) % len(xs)]

    pos = (n - 1) % (len(col) * 2)
    pos = min(pos, len(col)) - max(pos - len(col), 0)

    col.insert(pos, n)

    shout = [col[0] for col in xs]

print("".join(map(str, shout)))
