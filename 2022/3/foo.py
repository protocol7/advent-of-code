import sys
from util import *

def parse(line):
    s = line.strip()
    m = int(len(s) / 2)
    return set(s[:m]), set(s[m:])

xs = list(map(parse, sys.stdin))

s = 0
for a, b in xs:
    x = item(a & b)

    if x.islower():
        p = ord(x) - ord("a") + 1
    else:
        p = ord(x) - ord("A") + 27

    s += p

print(s)
