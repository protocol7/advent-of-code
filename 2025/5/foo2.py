#!/usr/bin/env python3

import sys
from util import *

def parse_a(line):
    return list(map(int, line.strip().split("-")))

a, _ = sys.stdin.read().strip().split("\n\n")

rs = list(map(parse_a, a.split("\n")))

intervals = Intervals()
for mi, ma in rs:
    intervals.add(Interval(mi, ma))

t = 0
for interval in intervals:
    t += interval.end - interval.start + 1

print(t)
