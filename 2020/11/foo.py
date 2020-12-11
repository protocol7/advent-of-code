import sys
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
            cc = sum(xs[yy][xx] == "#" for xx, yy in iter_adjacent(x, y, xs))

            nc = c
            if c == "L" and cc == 0:
                nc = "#"
            elif c == "#" and cc >= 4:
                nc = "L"
            nl += nc

        new.append(nl)

    xs = tuple(new)