#!/usr/bin/env python3

import sys
from util import chunks

ps = {
    "A": 0,
    "B": 1,
    "C": 3,
    "D": 5,
}

xs = chunks(sys.stdin.read().strip(), 3)

s = 0
for x in xs:
    boost = 2 - x.count("x")
    a, b, c = x

    a = ps[a] + boost if a != "x" else 0
    b = ps[b] + boost if b != "x" else 0
    c = ps[c] + boost if c != "x" else 0

    s += a + b + c

print(s)
