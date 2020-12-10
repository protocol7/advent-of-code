import sys
from collections import *
from itertools import *
from util import *

d = defaultdict(set)
for line in sys.stdin:
    if "contain no other bags" in line:
        continue

    xs = line.strip().split()
    bag = tuple(xs[:2])

    x = xs[4:]
    for i in range(0, len(x), 4):
        d[(x[i+1], x[i+2])].add(bag)


visited = set()
def walk(dd):
    for x in dd:
        visited.add(x)
        walk(d[x])

walk(d[("shiny", "gold")])
print(len(visited))