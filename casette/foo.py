#!/usr/bin/env python3

# https://casette.csokavar.hu/

import sys
from util import ints, sign, chunks

def parse(line):
    return list(map(sign, ints(line.strip())))

xs = list(map(parse, sys.stdin))

ds = []
for x in xs:
    n_ups = 0
    last_up = False
    counted = False
    for c in x:
        if c > 0 and last_up and not counted:
            n_ups += 1
            counted = True
        elif c > 0:
            last_up = True
        elif c < 0:
            last_up = False
            counted = False

    ds.append(n_ups // 4 - 1)

s = ""
for d in chunks(ds, 8):
    assert d[0] == 0
    assert d[-1] == 2
    assert d[-2] == 1
    s += chr(int("".join(map(str, d[1:-2])), 3))

print(s)
