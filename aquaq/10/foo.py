import sys
from collections import *
from itertools import *
from util import *

def parse(line):
    line = line.strip()
    if line == "s,d,c":
        return None

    a, b, c = line.split(",")

    return a, b, int(c)

xs = list(map(parse, sys.stdin))[1:]

d = defaultdict(dict)
for a, b, c in xs:
    d[a][b] = c
    d[b][a] = c

p = dijkstra(d, "TUPAC", "DIDDY")

print(p[1])