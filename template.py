#!/usr/bin/env python3

import sys
from collections import *
from itertools import *
from util import *

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

for x in xs:
    print(x)
