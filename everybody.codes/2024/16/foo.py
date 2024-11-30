#!/usr/bin/env python3

import sys
from collections import *
from itertools import *
from util import *


a, b = sys.stdin.read().strip().split("\n\n")

turns = ints(a)

bs = b.split("\n")

wheels = [[], [], [], []]

for line in bs:
    if not line:
        continue

    x = line[0:4].strip()
    y = line[4:8].strip()
    z = line[8:12].strip()
    w = line[12:].strip()

    if x:
        wheels[0].append(x)
    if y:
        wheels[1].append(y)
    if z:
        wheels[2].append(z)
    if w:
        wheels[3].append(w)

def turn_wheel(wheel, by):
    c = cycle(wheel)
    return list(islice(c, by, by + len(wheel)))

def visible(wheels):
    return [w[0] for w in wheels]

def points(visible):
    c = Counter(visible.replace(" ", ""))
    s = 0
    for v in c.values():
        if v < 3:
            continue
        s += v - 2
    return s

for _ in range(100):
    for i, (turn, wheel) in enumerate(zip(turns, wheels)):
        wheels[i] = turn_wheel(wheel, turn)

print(" ".join(visible(wheels)))
