import sys
from util import *

def parse(line):
    return ints(line.strip())

xs = list(map(parse, sys.stdin))

winning = [12, 48, 30, 95, 15, 55, 97]

s = 0
for x in xs:
    w = sum(1 for d in x if d in winning)

    if w >= 3:
        s += 10**(w-3)

print(s)