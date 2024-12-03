#!/usr/bin/env python3

import sys
import re

xs = sys.stdin.read()

p = r"mul\((\d+),(\d+)\)"

print(sum(int(m[0]) * int(m[1]) for m in re.findall(p, xs)))


