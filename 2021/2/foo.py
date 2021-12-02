import sys
from util import *

def parse(line):
    return intify(line.strip().split())

xs = map(parse, sys.stdin)

h = 0
d = 0

for a, b in xs:
    if a == "forward":
        h += b
    elif a == "down":
        d += b
    elif a == "up":
        d -= b

print(h * d)