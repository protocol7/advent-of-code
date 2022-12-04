import sys
from util import *

def parse(line):
    return ints(line.strip(), negatives=False)

xs = list(map(parse, sys.stdin))

p1 = 0
p2 = 0
for a, b, c, d in xs:
    s1 = Span(a, b)
    s2 = Span(c, d)

    if s1 in s2 or s2 in s1:
        p1 += 1

    if s1 & s2:
        p2 += 1

print(p1)
print(p2)