#!/usr/bin/env python3

import sys
from collections import deque
from util import Grid, ORTHOGONAL

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

g = Grid(xs)


def perimeter(outside):
    seen = set()
    s = 0
    for p, d in outside:
        if (p, d) in seen:
            continue
        seen.add((p, d))

        q = deque([p])
        s += 1

        while q:
            p = q.popleft()

            for n, _v in g.orthogonal(p):
                if (n, d) in seen:
                    continue

                if (n, d) in outside:
                    q.append(n)
                    seen.add((n, d))

    return s

seen = set()
price = 0
for p, v in g.points():
    if p in seen:
        continue
    seen.add(p)

    outside = set()
    area = set([p])

    q = deque([p])

    while q:
        p = q.popleft()

        for dir in ORTHOGONAL:
            n = p + dir
            nv = g[n]
            if nv != v:
                outside.add((n, dir))
                continue

            if nv == v and n not in seen:
                area.add(n)
                seen.add(n)
                q.append(n)

    price += len(area) * perimeter(outside)

print(price)
