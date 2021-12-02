import sys
from util import *

def parse(line):
    return intify(line.strip().split())

xs = map(parse, sys.stdin)

h = 0
d = 0
aim = 0

for a, b in xs:
    if a == "forward":
        h += b
        d += b * aim
    elif a == "down":
        aim += b
    elif a == "up":
        aim -= b

print(h * d)
