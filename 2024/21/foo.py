#!/usr/bin/env python3

import sys
from collections import deque
from functools import cache

numeric_pad = {
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "0": (1, 3),
    "A": (2, 3),
}

dpad_pad = {
    "^": (1, 0),
    "A": (2, 0),
    "<": (0, 1),
    "v": (1, 1),
    ">": (2, 1),
}

def paths(pad, start, end):
    def valid(x, y):
        return (x, y) in pad.values()

    ex, ey = pad[end]

    q = deque([(pad[start], "")])
    while q:
        (x, y), dirs = q.popleft()

        if (x, y) == (ex, ey):
            yield dirs

        if x > ex and valid(x - 1, y):
            # try left
            q.append(((x - 1, y), dirs + "<"))
        if x < ex and valid(x + 1, y):
            # try right
            q.append(((x + 1, y), dirs + ">"))
        if y > ey and valid(x, y - 1):
            # try up
            q.append(((x, y - 1), dirs + "^"))
        if y < ey and valid(x, y + 1):
            # try down
            q.append(((x, y + 1), dirs + "v"))

@cache
def robots(dirs, n_robots):
    dirs = dirs + "A"
    if n_robots == 1:
        return len(dirs)

    dirs = "A" + dirs

    s = 0
    for a, b in zip(dirs, dirs[1:]):
        s += min(robots(path, n_robots-1) for path in paths(dpad_pad, a, b))

    return s

def numeric(x, n_robots):
    x = "A" + x

    s = 0
    for a, b in zip(x, x[1:]):
        m = sys.maxsize
        for path in paths(numeric_pad, a, b):
            m = min(m, robots(path, n_robots))

        s += m
    return s

def foo(xs, n_robots):
    return sum(numeric(x, n_robots) * int(x[:-1]) for x in xs)

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

print(foo(xs, 3))
print(foo(xs, 26))
