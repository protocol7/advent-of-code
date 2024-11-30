#!/usr/bin/env python3

import sys
from collections import *
from itertools import *
from util import *
import re


a, b = sys.stdin.read().strip().split("\n\n")

ws = a.split(":")[1].split(",")

ws = ws + [w[::-1] for w in ws]

p = [False] * len(b)

def findall(s, substring):
    for i, c in enumerate(s):
        if s[i:i+len(substring)] == substring:
            yield i

s = 0
for w in ws:
    indexes = list(findall(b, w))

    for i in indexes:
        for j in range(len(w)):
            p[i + j] = True

print(p.count(True))
