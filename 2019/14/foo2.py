import sys
from collections import *
from math import ceil
from util import *

def parse(line):
    x = intify(reversed(tokens(line)))
    return x[:2], chunks(x[2:], 2)

parsed = map(parse, sys.stdin)

# build dict of material -> needs, to get dependency order
g = defaultdict(list)
for (po, pn), pi in parsed:
    for p, _ in pi:
        g[po].append(p)

# get the order in which we need to resolve dependencies, using topological
# sort. Start from FUEL.
order = top_sort(g, "FUEL")
order = order[:-1] # don't include "ORE"

# build recipes of material -> how much is produced, and what's needed
r = dict()
for (po, pn), pi in parsed:
    r[po] = [pn, pi]

# resolve needs
# what's currently needed
need = defaultdict(int)
need["FUEL"] = 1

# what's the next thing I need?
for nm in order:
    # how much do I need?
    na = need[nm]
    # how much is produced, and from what
    np, mm = r[nm]
    # only difference from part 1
    # what's the exact conversion rate, e.g. if 28 is needed, 10 is produced for each
    # input, this gives 28 / 10 -> 2.8
    cr = float(na) / np
    # add needs for each material needed
    for mt, ma in mm:
        need[mt] += ma * cr

    # we've fulfilled this need, remove
    del need[nm]

print(int(1000000000000 / need["ORE"]))
