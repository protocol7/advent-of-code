import sys
from collections import *
from itertools import *
from util import *

def parse(line):
    _, a, b = line.strip().split()

    return b, int(a)

xs = list(map(parse, sys.stdin))

c = Counter()
for a, b in xs:
    c[a] += b

p = 1
for v in c.values():
    p *= v % 100

print(p)