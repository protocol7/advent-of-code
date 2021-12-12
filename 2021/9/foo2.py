import sys
from util import *

def parse(line):
    return list(map(int, line.strip()))

g = list(map(parse, sys.stdin))

basins = []

for x, y, c in iter_grid(g):
    if c == 9:
        continue

    ns = []
    for xx, yy in iter_orthogonal(x, y, g):
        if g[yy][xx] == 9:
            continue
        
        # collect basins that orthogonal neighbours are in
        for b in basins:
            if (xx, yy) in b:
                ns.append(b)

    if ns:
        # merge basins
        s = set()
        for n in ns:
            s.update(n)
            if n in basins:
                basins.remove(n)

        s.add((x, y))
        basins.append(s)
    else:
        # new basin
        basins.append(set([(x, y)]))

basins = sorted(basins, key=lambda x: -len(x))

print(product(len(x) for x in basins[:3]))
