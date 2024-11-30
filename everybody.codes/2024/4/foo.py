#!/usr/bin/env python3

import sys
from collections import *
from itertools import *
from util import *


def parse(line):
    return int(line.strip())


xs = list(map(parse, sys.stdin))

m = min(xs)

print(sum(x - m for x in xs))
