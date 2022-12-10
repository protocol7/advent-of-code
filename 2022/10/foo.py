import sys
from util import *

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

x = 1
xx = []

for a in xs:
    xx += [x]
    if a.startswith("addx"):
        xx += [x]

        x += ints(a)[0]

print(sum(xx[c-1] * c for c in (20, 60, 100, 140, 180, 220)))

crt = []
for i, x in enumerate(xx):
    if x - 1 <= i % 40 <= x+1:
        crt.append("#")
    else:
        crt.append(" ")

for c in chunks(crt, 40):
    print(join(c))
