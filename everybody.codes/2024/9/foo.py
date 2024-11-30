#!/usr/bin/env python3

import sys
from collections import *
from itertools import *
from util import *


def parse(line):
    return int(line.strip())


xs = list(map(parse, sys.stdin))

stamps = [1, 3, 5, 10]

s = 0
for x in xs:
    for c in count(1):
        stamp = max(s for s in stamps if s <= x)

        x -= stamp

        if x == 0:
            break

    s += c

print(s)
