#!/usr/bin/env python3

import sys
from itertools import count
from util import Grid, turn_left, turn_right, DOWN

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

g = Grid(xs)

def run():
    start = g.points_by_value()["S"][0]
    best = {(start, DOWN, "ABCS"): 10000}

    for time in count():
        nbest = {}
        for (p, dir, targets), alt in best.items():
            if not targets:
                if alt >= 10000:
                    return time
                else:
                    continue

            for ndir in [dir, turn_left(dir), turn_right(dir)]:
                np = p + ndir
                v = g[np]
                if v == '#' or v == None:
                    continue

                new_targets = targets
                if v == ".":
                    gain = -1
                elif v in "ABCS":
                    gain = -1
                    if v == targets[0]:
                        new_targets = targets[1:]
                elif v == "+":
                    gain = 1
                elif v == "-":
                    gain = -2
                else:
                    assert False, v

                xx = (np, ndir, new_targets)
                nbest[xx] = max(nbest.get(xx, -1), alt + gain)

        best = nbest

print(run())
