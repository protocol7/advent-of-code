import sys
from collections import *
from itertools import *
from util import *

def parse(line):
    return line.strip("\n")

xs = list(map(parse, sys.stdin))

g = Grid(xs)

clear = "FISSION_MAILED"
crypt = ""

for c in clear:
    # find starting point
    for p, v in g.points():
        if p.x == 0 and v == c:
            break

    dir = RIGHT

    # step out
    p += dir

    while g[p] in " \/":
        v = g[p]

        if v == "\\":
            if dir == RIGHT:
                dir = DOWN
            elif dir == DOWN:
                dir = RIGHT
            elif dir == UP:
                dir = LEFT
            elif dir == LEFT:
                dir = UP

            g.d[p] = "/"
        elif v == "/":
            if dir == RIGHT:
                dir = UP
            elif dir == DOWN:
                dir = LEFT
            elif dir == UP:
                dir = RIGHT
            elif dir == LEFT:
                dir = DOWN

            g.d[p] = "\\"

        p += dir

    crypt+= g[p]

print(crypt)
