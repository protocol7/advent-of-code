#!/usr/bin/env python3

import sys
import re

xs = sys.stdin.read()

p = r"(?:mul\((\d+),(\d+)\))|(do\(\))|(don\'t\(\))"

t = 0
do = True
for m in re.findall(p, xs):
    if m[2]:
        do = True
    elif m[3]:
        do = False
    elif do:
        t += int(m[0]) * int(m[1])

print(t)


