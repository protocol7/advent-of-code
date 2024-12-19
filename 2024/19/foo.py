#!/usr/bin/env python3

import sys
from functools import cache

a, b = sys.stdin.read().strip().split("\n\n")

patterns = a.split(", ")
words = b.split()

@cache
def foo(rem):
    if not rem:
        return 1

    s = 0
    for pattern in patterns:
        if rem.startswith(pattern):
            s += foo(rem[len(pattern):])

    return s

print(sum(bool(foo(word)) for word in words))
print(sum(foo(word) for word in words))
