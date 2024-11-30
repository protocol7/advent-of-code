#!/usr/bin/env python3

import sys
from util import chunks

ps = {
    "x": 0,
    "A": 0,
    "B": 1,
    "C": 3,
    "D": 5,
}

xs = chunks(sys.stdin.read(), 2)

s = 0
for x in xs:
    boost = "x" not in x
    a, b = x

    a = ps[a] + boost
    b = ps[b] + boost

    s += a + b

print(s)
