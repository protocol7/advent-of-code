#!/usr/bin/env python3

import sys
from collections import *
from itertools import *
from util import *


def parse(line):
    a, b = line.strip().split(":")
    return a, b.split(",")


xs = list(map(parse, sys.stdin))

out = []
for a, bs in xs:
    p = 10

    s = 0
    for i, b in enumerate(cycle(bs)):
        if i == 10:
            break


        if b == "=":
            pass
        elif b == "+":
            p += 1
        elif b == "-" and p > 0:
            p -= 1
        else:
            assert False

        s += p
        #print(i, b, p, s)

    out.append((a, s))

out = sorted(out, key=lambda x: x[1], reverse=True)
print("".join(x[0] for x in out))
