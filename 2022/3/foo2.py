import sys
from util import *

def parse(line):
    return set(line.strip())

xs = list(map(parse, sys.stdin))

s = 0
for a, b, c in chunks(xs, 3):
    x = item(a & b & c)

    if x.islower():
        p = ord(x) - ord("a") + 1
    else:
        p = ord(x) - ord("A") + 27

    s += p

print(s)
