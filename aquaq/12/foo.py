import sys
from collections import *
from itertools import *
from util import *

def parse(line):
    return ints(line.strip())

xs = list(map(parse, sys.stdin))

fs = {}
for i, (a, b) in enumerate(xs):
    fs[i] = (a, b)

f = 0
d = 1

c = 0
while f in fs:
    c += 1

    a, b = fs[f]

    if a == 0:
        d *= -1

    f += b * d

print(c + 1)