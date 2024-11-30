#!/usr/bin/env python3

import sys
from collections import *
from itertools import *
from util import *
import re


a, b = sys.stdin.read().strip().split("\n\n")

ws = a.split(":")[1].split(",")

ws = ws + [w[::-1] for w in ws]

b = b.split("\n")

p = []
for bb in b:
    p.append([False] * len(bb))

def findall(s, substring):
    for i, c in enumerate(s):
        if s[i:i+len(substring)] == substring:
            yield i


for w in ws:
    for bb, pp in zip(b, p):
        indexes = list(findall(bb + bb, w))

        for i in indexes:
            for j in range(len(w)):
                pp[(i + j) % len(bb)] = True

    for col in range(len(b[0])):
        bb = "".join([row[col] for row in b])

        indexes = list(findall(bb, w))

        for i in indexes:
            for j in range(len(w)):
                p[i + j][col] = True

s = 0
for bb, pp in zip(b, p):
    s += pp.count(True)

print(s)
