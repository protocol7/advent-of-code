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

        # pre filter to speed things up
        c = Counter()
        for ff in xs:
            x, y, vx, vy = ff
            x = (x + vx) % w
            y = (y + vy) % h

            ff[0] = x
            ff[1] = y

            c[y] += 1
            d[(x, y)] = "#"

        if c.most_common(1)[0][1] > 20:
            g = Grid(d)

            for row in g.rows():
                s = str(row)

                if "########" in s:
                    print(i)
                    g.pretty_print()

                    return

run()
