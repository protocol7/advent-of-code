#!/usr/bin/env python3

import sys
from collections import deque
from util import Grid

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

g = Grid(xs)

seen = set()

price = 0
for p, v in g.points():
    if p in seen:
        continue
    seen.add(p)

    perimeter = 0
    area = 1

    q = deque([p])

    while q:
        p = q.popleft()

        for n, nv in g.orthogonal(p):
            if nv != v:
                perimeter += 1
                continue

            if nv == v and n not in seen:
                area += 1
                seen.add(n)
                q.append(n)

    price += area * perimeter

print(price)
