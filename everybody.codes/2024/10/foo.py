#!/usr/bin/env python3

import sys
from collections import *
from itertools import *
from util import *


def parse(line):
    return line.strip()


xs = list(map(parse, sys.stdin))

rows = []
for x in xs:
    if x[0] != "*":
        rows.append(set(x.replace(".", "")))

cols = []
for x in transpose(xs):
    if x[0] != "*":
        cols.append(set("".join(x).replace(".", "")))

s = ""
for r in range(4):
    for c in range(4):
        s += item(rows[r] & cols[c])

print(s)
