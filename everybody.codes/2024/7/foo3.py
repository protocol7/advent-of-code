#!/usr/bin/env python3

import sys
from collections import *
from itertools import *
from util import *

# track

def load_track():
    with open("track3.txt") as f:
        lines = [line.strip() for line in f.readlines()]
        g = Grid(lines)

        p = g.points_by_value()["S"][0]
        track = [p]
        trackv = [g[p]]
        # start to the right
        p = Point(p.x + 1, p.y)
        track += [p]
        trackv += [g[p]]

        while True:
            found = False
            for n, v in g.orthogonal(p):
                if v is not None and v != " " and n not in track:
                    track += [n]
                    trackv += [g[n]]
                    p = n
                    found = True
                    break

            if not found:
                break

        trackv += trackv.pop(0)
        return "".join(trackv)

track = load_track()

print(track)

# race

def parse(line):
    a, b = line.strip().split(":")
    return a, b.split(",")


xs = list(map(parse, sys.stdin))

def race(bs):
    p = 10
    s = 0

    bs = cycle(bs)

    for loop in range(2024):
        for t, b in zip(track, bs):
            if t == "=" or t == "S":
                if b == "=":
                    pass
                elif b == "+":
                    p += 1
                elif b == "-" and p > 0:
                    p -= 1
                else:
                    assert False
            elif t == "+":
                p += 1
            elif t == "-" and p > 0:
                p -= 1
            else:
                assert False

            s += p

    return s

other = race(xs[0][1])
print(other)

print(sum(1 for _ in permutations("+++++---===")))

s = 0
t = 0
n = 0
seen = set()
for p in permutations("+++++---==="):
    n += 1
    if p in seen:
        continue
    seen.add(p)

    res = race(p)

    if res > other:
        s += 1

    t += 1

    if t % 100 == 0:
        print(n, t, s, res, p)

print(s)
