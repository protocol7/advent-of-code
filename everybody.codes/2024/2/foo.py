#!/usr/bin/env python3

import sys
from collections import *
from itertools import *
from util import *


a, b = sys.stdin.read().strip().split("\n\n")

ws = a.split(":")[1].split(",")

s = 0
for w in ws:
    s += b.count(w)

print(s)
