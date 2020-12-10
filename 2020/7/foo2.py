import sys
from collections import *

d = defaultdict(set)
for line in sys.stdin:
    if "contain no other bags" in line:
        continue

    xs = line.strip().split()

    bag = tuple(xs[:2])

    x = xs[4:]
    for i in range(0, len(x), 4):
        b = (int(x[i]), x[i+1], x[i+2])
        d[bag].add(b)


def walk(dd):
    cnt = 0
    for a, b, c in dd:
        x = (b, c)
        cnt += a
        cnt += walk(d[x]) * a

    return cnt


print(walk(d[("shiny", "gold")]))