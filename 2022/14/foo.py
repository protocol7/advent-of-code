import sys
from itertools import *
from util import *

def parse(line):
    return chunks(ints(line), 2)

xs = list(map(parse, sys.stdin))

d = set()
for row in xs:
    for (x1, y1), (x2, y2) in zip(row, row[1:]):
        for x in diffrange(x1, x2):
            for y in diffrange(y1, y2):
                d.add((x, y))

maxy = max(y for _, y in d)

part1 = True
for c in count():
    sx, sy = (500, 0)

    while True:
        if sy == maxy + 1:
            if part1:
                print(c)
                part1 = False

            # on bottom floor, rest
            d.add((sx, sy))
            break
        elif (sx, sy+1) not in d:
            # point below is free
            sy += 1
        elif (sx-1, sy+1) not in d:
            # point below and to the left is free
            sx -= 1
            sy += 1
        elif (sx+1, sy+1) not in d:
            # point below and to the right is free
            sx += 1
            sy += 1
        elif (sx, sy) not in d:
            # we can't move down and we haven't fill up all the way, rest here
            d.add((sx, sy))
            break
        else:
            # filled up all the way, we're done with part 2
            print(c)
            sys.exit()