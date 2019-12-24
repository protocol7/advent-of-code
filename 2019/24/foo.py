import sys
from collections import *

def parse(line):
    return line.strip()

m = tuple(map(parse, sys.stdin))

def pp(m):
    for line in m:
        print("".join(line))
    print("")


w = 5
h = 5

adjacent = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def tick(m):
    mm = []
    for y, line in enumerate(m):
        ll = []
        for x, c in enumerate(line):
            n = 0
            for dx, dy in adjacent:
                ax = x + dx
                ay = y + dy
                if ax < 0 or ay < 0 or ax >= w or ay >= h:
                    continue
                cc = m[ay][ax]
                if cc == "#":
                    n += 1

            if c == "#":
                if  n == 1:
                    ll.append("#")
                else:
                    ll.append(".")
            elif c == ".":
                if  n == 1 or n == 2:
                    ll.append("#")
                else:
                    ll.append(".")
            else:
                assert False
        mm.append("".join(ll))
    return tuple(mm)

def bio(m):
    p = 1
    s = 0
    for line in m:
        for c in line:
            if c == "#":
                s += p
            p *= 2
    return s

pp(m)
seen = set([m])

while True:
    m = tick(m)

    if m in seen:
        pp(m)
        break
    seen.add(m)

print(bio(m))
