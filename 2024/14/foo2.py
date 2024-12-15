#!/usr/bin/env python3

import sys
from collections import *
from itertools import *
from util import *

def parse(line):
    return ints(line.strip())

xs = list(map(parse, sys.stdin))

w = 101
h = 103

def run():
    for i in count(1):
        d = {}

        for ff in xs:
            x, y, vx, vy = ff
            x = (x + vx) % w
            y = (y + vy) % h

            ff[0] = x
            ff[1] = y

            d[(x, y)] = "#"

        g = Grid(d)

        for row in g.rows():
            s = str(row)

            if "########" in s:
                print(i)
                g.pretty_print()

                return

run()
