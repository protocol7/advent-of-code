import sys
from util import *

def parse(line):
    return ints(line.strip())

xs = list(map(parse, sys.stdin))

d = defaultdict(bool)
for x, y, w, h in xs:
    for xx in range(x, x + w):
        for yy in range(y, y + h):
            k = (xx, yy)
            d[k] = not d[k]

for y in range(10):
    s = ""
    for x in range(50):
        k = (x, y)

        if d[k]:
            s += "#"
        else:
            s += "."

    print(s)