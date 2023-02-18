import sys
from util import *
from math import sqrt

def parse(line):
    return ints(line.strip())

xs = list(map(parse, sys.stdin))

s = 0
for a, b in zip(xs, xs[1:]):
    x = a[0] - b[0]
    y = a[1] - b[1]
    z = a[2] - b[2]

    s += int(sqrt(x*x + y*y + z*z))

print(s)