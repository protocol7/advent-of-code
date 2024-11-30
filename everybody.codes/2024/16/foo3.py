#!/usr/bin/env python3

import sys
sys.setrecursionlimit(10000)

from collections import Counter
from itertools import cycle, islice
from util import chunks, ints
from functools import cache


a, b = sys.stdin.read().strip().split("\n\n")

turns = ints(a)

bs = b.split("\n")

wheels = []
for i in range(len(turns)):
    wheels.append([])


for line in bs:
    if not line:
        continue

    xs = chunks(line, 4)

    for i, x in enumerate(xs):
        x = x.strip()
        if x:
            wheels[i].append(x)

def turn_wheel(wheel, by):
    c = cycle(wheel)
    return list(islice(c, by, by + len(wheel)))

def visible(wheels):
    return [w[0] for w in wheels]

def points(wheels):
    vv = "".join(visible(wheels))

    no_muzzles = ""
    for i in range(0, len(vv), 3):
        no_muzzles += vv[i] + vv[i + 2]

    c = Counter(no_muzzles)
    return sum(v - 2 for v in c.values() if v >= 3)

max_rounds = 256

@cache
def rec(round, offset):
    if round > max_rounds:
        return (0, 0)

    if round > 0:
        ws = wheels[:]
        for i, (turn, wheel) in enumerate(zip(turns, ws)):
            t = (turn * round + offset) % len(wheel)
            ws[i] = turn_wheel(wheel, t)

        p = points(ws)
    else:
        p = 0

    ps = []
    for o in (-1, 0, 1):
        ps.append(rec(round + 1, offset + o))

    return p + max(pp[0] for pp in ps), p + min(pp[1] for pp in ps)


print(" ".join(map(str, rec(0, 0))))
