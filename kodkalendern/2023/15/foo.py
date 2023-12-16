import sys
from util import *

def parse(line):
    return ints(line.strip())

xs = list(map(parse, sys.stdin))

t = 0
for x in xs:
    ok = True
    for a, b, c  in zip(x, x[1:], x[2:]):
        if b <= a or c <= b:
            ok = False
        elif c - b <= b - a:
            ok = False

    if not ok:
        t += 1

print(t)
