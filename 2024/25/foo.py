#!/usr/bin/env python3

import sys

xs = sys.stdin.read().strip().split("\n\n")

keys = []
locks = []
for x in xs:
    x = x.strip().split("\n")

    if x[0] == "#####":
        tmp = locks
        xz = x[1:]
    else:
        tmp = keys
        xz = x[:-1][::-1]

    heights = [0] * len(x[0])
    for xx in xz:
        for i, c in enumerate(xx):
            if c == "#":
                heights[i] += 1

    tmp.append(heights)

t = 0
for key in keys:
    for lock in locks:
        hs = [a + b for a, b in zip(key, lock)]

        if all(h < 6 for h in hs):
            t += 1

print(t)
