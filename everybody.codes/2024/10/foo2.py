#!/usr/bin/env python3

import sys
from collections import *
from itertools import *
from util import *


def parse(line):
    return line.strip()

xs = sys.stdin.read().strip().split("\n\n")

ds = []
for x in xs:
    rs = []
    x = x.splitlines()

    for row in x:
        row = row.split()
        for i, t in enumerate(row):
            if len(rs) < i + 1:
                rs.append([])
            rs[i].append(t)

    ds.extend(rs)

print(ds)

def word(xs):
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

    return s

words = [word(d) for d in ds]

def power(word):
    p = 0
    for i, c in enumerate(word):
        p += (i + 1) * (ord(c) - ord("A") + 1)
    return p

print(power("PTBVRCZHFLJWGMNS"))

print(sum(power(w) for w in words))
