import sys
from itertools import *
from util import *

def parse(line):
    return ints(line.strip())

xs = list(map(parse, sys.stdin))

PS = (
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9},

    {1, 4, 7},
    {2, 5, 8},
    {3, 6, 9},

    {1, 5, 9},
    {3, 5, 7},
)

xw = 0
ow = 0
d = 0
for ms in xs:
    x = set()
    o = set()

    def won(ds):
        for p in PS:
            if p & ds == p:
                return True

    for oo, xx in zip_longest(ms[::2], ms[1::2]):
        o.add(oo)
        x.add(xx)

        if won(o):
            ow += 1
            break
        elif won(x):
            xw += 1
            break
    else:
        d += 1

print(ow * xw * d)