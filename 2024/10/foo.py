#!/usr/bin/env python3

import sys
from collections import deque
from util import Grid

def parse(line):
    return list(map(int, line.strip()))

xs = list(map(parse, sys.stdin))

g = Grid(xs)

starts = g.points_by_value()[0]

t = 0
t2 = 0
for start in starts:
    ends = set()
    paths = 0

    q = deque([start])
    while q:
        p = q.popleft()
        v = g[p]

        if v == 9:
            ends.add(p)
            paths += 1
            continue

        for n, nv in g.orthogonal(p):
            if nv == v + 1:
                q.append(n)

    t += len(ends)
    t2 += paths

print(t)
print(t2)
