import sys
from util import *

def parse(line):
    return ints(line.strip())

xs = list(map(parse, sys.stdin))

sx = [(x, y, x+w-1, y+h-1) for x, y, w, h in xs]

area = 0
h = 100000
w = 20000
for y in range(h):
    ix = Intervals()

    for x0, y0, x1, y1 in sx:
        if y0 <= y <= y1:
            ix.add(Interval(x0, x1))
            
    area += w - sum(len(i) for i in ix.intervals)

print(area)