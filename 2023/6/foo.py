import sys
from util import *


def parse(line):
    return ints(line.strip())


xs = list(map(parse, sys.stdin))

t = 1
for a, b in zip(xs[0], xs[1]):
    w = 0
    for i in range(a+1):
        d = i * (a - i)

        w += d > b

    t *= w

print(t)
