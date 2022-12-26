import sys
from collections import *
from itertools import *
from util import *

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

def find_next(x):
    d = int(x)

    for i in range(2, len(x)+1):
        # shuffle last i chars
        prefix = x[:-i]
        suffix = x[-i:]
        
        mm = None
        for p in permutations(suffix):
            p = int(prefix + join(p))

            if p > d:
                if mm is None:
                    mm = p
                else:
                    mm = min(mm, p)

        if mm is None:
            continue
        else:
            return mm

s = 0
for x in xs:
    n = find_next(x)

    x = int(x)
    if n is None:
        n = x
    s += n - x

print(s)
