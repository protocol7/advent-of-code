import sys
from itertools import *
from util import *

def parse(line):
    return line.strip()

xs = tuple(map(parse, sys.stdin))

seen = set()

while True:
    if xs in seen:
        print(sum(line.count("#") for line in xs))
        break
    seen.add(xs)

    new = list()
    for y, line in enumerate(xs):
        nl = ""

        for x, c in enumerate(line):
            cc = 0
            for dx, dy in adjacent:
                for l in count(1):
                    xx = x + dx * l
                    yy = y + dy * l

                    g = grid_get(xs, xx, yy)

                    if g is None:
                        break
                    if g == "#":
                        cc += 1
                        break
                    elif g == "L":
                        break

            nc = c
            if c == "L" and cc == 0:
                nc = "#"
            elif c == "#" and cc >= 5:
                nc = "L"
            nl += nc

        new.append(nl)

    xs = tuple(new)