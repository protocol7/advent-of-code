import sys
from collections import *
from itertools import *
from util import *

def parse(line):
    return ints(line)

xs = list(map(parse, sys.stdin))

v = 0
for a, b, c in xs:
    if a != 7 and b != 7 and c != 7:
        v += a * b * c

print(v)