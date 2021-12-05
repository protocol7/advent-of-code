import sys
from collections import *
from util import *

def parse(line):
    return ints(line.strip())

xs = list(map(parse, sys.stdin))

def run(part2):
    c = Counter()

    for x1, y1, x2, y2 in xs:
        if part2 or x1 == x2 or y1 == y2:
            x = x1
            y = y1

            while x != x2 or y != y2:
                c[(x, y)] += 1

                x += sign(x2 - x1)
                y += sign(y2 - y1)

            c[(x, y)] += 1

    print(sum([1 for b in c.values() if b > 1]))

run(False)
run(True)