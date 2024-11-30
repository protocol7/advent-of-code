#!/usr/bin/env python3

import sys
from collections import *
from itertools import *
from util import *


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

def points(visible):
    no_muzzles = ""
    for i in range(0, len(visible), 3):
        no_muzzles += visible[i] + visible[i + 2]

    c = Counter(no_muzzles)
    s = 0
    for v in c.values():
        if v < 3:
            continue
        s += v - 2
    return s

wheel_sizes = [len(w) for w in wheels]

rounds = 202420242024

def run(n_turns):
    total = 0
    for r in range(n_turns):
        for i, (turn, wheel) in enumerate(zip(turns, wheels)):
            wheels[i] = turn_wheel(wheel, turn)

        total += points("".join(visible(wheels)))

    return total

rotates_after = lcm(*wheel_sizes)

base_total = run(rotates_after)
extra_total = run(rounds % rotates_after)

print((base_total * (rounds // rotates_after)) + extra_total)
