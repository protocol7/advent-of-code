import sys
from collections import *
from itertools import *
from util import *

def parse(line):
    return ints(line)

xs = list(map(parse, sys.stdin))

for i, (a, b, c) in enumerate(xs):
    if a * b != c:
        print(i)