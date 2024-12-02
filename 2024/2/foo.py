#!/usr/bin/env python3

import sys
from util import ints, sign

xs = map(ints, sys.stdin)

def safe(x):
    diffs = []
    signs = set()
    for a, b in zip(x, x[1:]):
        diffs.append(abs(b - a))
        signs.add(sign(b - a))

    return len(signs) == 1 and all(1 <= d <= 3 for d in diffs)

t1 = 0
t2 = 0
for x in xs:
    if safe(x):
        t1 += 1
        t2 += 1
    else:
        for i in range(len(x)):
            if safe(x[:i] + x[i+1:]):
                t2 += 1
                break

print(t1)
print(t2)
