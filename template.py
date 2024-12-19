#!/usr/bin/env python3

import sys
from collections import *
from itertools import *
from util import *
from functools import *

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))
# a, b = sys.stdin.read().strip().split("\n\n")

for x in xs:
    print(x)
