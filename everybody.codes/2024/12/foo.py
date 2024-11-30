#!/usr/bin/env python3

import sys
from collections import *
from itertools import *
from util import *


def parse(line):
    return line.strip()


xs = list(map(parse, sys.stdin))

g = Grid(xs)

ts = g.points_by_value()["T"]
for h in g.points_by_value()["H"]:
    ts.append(h)
    ts.append(h)

segments = [(g.points_by_value()[p][0], i+1) for i, p in enumerate("ABC")]

print(segments)
print(ts)

earth = max(ts, key=lambda t: t.y).y + 1

out = 0
for t in ts:
    rankings = []
    for s, n in segments:
        dx = t.x - s.x
        dy = t.y - s.y

        assert dx >= 0, dx

        for power in range(1, dx+1):
            x = s.x
            y = s.y

            for d in range(0, power):
                x += 1
                y -= 1

                if t.x == x and t.y == y:
                    rankings.append((n, power, n * power))
                    break

            for d in range(0, power):
                x += 1

                if t.x == x and t.y == y:
                    rankings.append((n, power, n * power))
                    break

            while y <= earth:
                x += 1
                y += 1

                if t.x == x and t.y == y:
                    rankings.append((n, power, n * power))
                    break

    assert len(rankings) == 1, rankings
    out += rankings[0][2]

print(out)
