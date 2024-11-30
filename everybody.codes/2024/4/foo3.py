#!/usr/bin/env python3

import sys

def parse(line):
    return int(line.strip())

xs = list(map(parse, sys.stdin))

# Ternary search algorithm to find the minimum of a
# unimodal function within a given range [l, r]
# From https://www.geeksforgeeks.org/find-the-minimum-value-of-a-unimodal-function/
def ternary_search(f, l, r):
    cnt = 300
    while cnt > 0:
        mid1 = l + (r - l) / 3.0
        mid2 = r - (r - l) / 3.0

        # Compare function values at mid1 and mid2 to
        # determine the search range
        if f(mid1) < f(mid2):
            r = mid2
        else:
            l = mid1

        cnt -= 1

    return f(l)

print(round(ternary_search(lambda m: sum(abs(x - m) for x in xs), min(xs), max(xs))))
