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

    mid = len(s) // 2

    if s[0:mid] == s[mid:]:
        t += y

print(t)


