import sys
from collections import *

def parse(line):
    return int(line.strip())

xs = sorted(list(map(parse, sys.stdin)))
t = max(xs) + 3
xs = [0] + xs + [t]

# build dict of node -> nodes that leads to it
ii = defaultdict(set)
for i, x in enumerate(xs):
    for k in xs[:i]:
        if x - k < 4:
            ii[x].add(k)

# for each node, sum up the number of paths that lead to it
levels = {0: 1}
for k, v in ii.items():
    levels[k] = sum(levels[x] for x in v)

print(levels[t])