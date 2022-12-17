import sys
from collections import *
from itertools import *
from util import *

def parse(line):
    return ints(line)

xs = list(map(parse, sys.stdin))

cs = 0
for a, b, c in xs:
    days = a * 16 * 26 + b * 26 + c

    if days >= 10000:
        cs += 1

print(cs)