import sys
from collections import *
from itertools import *
from util import *

def parse(line):
    return int(line.strip())

xs = list(map(parse, sys.stdin))

ms = []
s = 0
for i, (a, b, c) in enumerate(chunks(xs, 3)):
    if a + b != c:
        ms.append(i * 3 + 2)
        s += a + b - c

print(ms)
print(s)