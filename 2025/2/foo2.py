#!/usr/bin/env python3

import sys

xs = sys.stdin.read().strip().split(",")

ys = []
for x in xs:
    a, b = map(int, x.split("-"))

    ys.extend(list(range(a, b+1)))

t = 0
for y in ys:
    s = str(y)

    for i in range(1, int(len(s) / 2) + 1):
        pat = s[0:i]
        mul = len(s) // i

        if pat * mul == s:
            t += y
            break

print(t)
