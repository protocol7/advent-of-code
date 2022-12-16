import sys
from itertools import combinations
from util import *
from functools import cache, reduce

def parse(line):
    x = line.strip().split()

    valve = x[1]
    rate = int(x[4].split("=")[1].strip(";"))

    cc = x[9:]
    cc = [c.strip(",") for c in cc]

    return valve, rate, cc

xs = list(map(parse, sys.stdin))

# create the graph, flow rates and 
d = {}
rates = {}
closed = set()
for v, r, c in xs:
    d[v] = [(cc, 1) for cc in c]
    rates[v] = r

    if r > 0:
        closed.add(v)

keep = set(closed)
keep.add("AA")

# compress graph by removing valves with zero flow rate. We compress until we can't compress more
while True:
    changed = False
    for n, cs in d.items():
        ncs = []
        for c, dist in cs:
            if c in keep:
                # child is non-zero valve or start, keep as is
                ncs.append((c, dist))
            else:
                changed = True
                # zero valve, skip over
                for cc, cdist in d[c]:
                    if cc == n:
                        continue
                    ncs.append((cc, dist + cdist))

        d[n] = ncs

    if not changed:
        break

# create map of nodes to integers
nodes = {n: i for i, n in enumerate(keep)}

# start
aa = nodes["AA"]

# convert the graph to integer identifiers
nd = {}
for n, cs in d.items():
    if n in keep:
        nd[nodes[n]] = [(nodes[c], dist) for c, dist in cs]
d = nd

# convert set of closed valus to integer identifiers
closed = set(nodes[c] for c in closed)

# convert flow rates to integer identifiers
rates = {nodes[n]: v for n, v in rates.items() if n in nodes}

# if we're at cur, have rem minutes left and have a set of still closed valves,
# what's the most pressure we can release?
@cache
def foo(cur, rem, closed, other_players):
    if rem <= 0:
        if other_players > 0:
            # let the elephant start once I've run out of time
            # stolen from https://www.youtube.com/watch?v=DgqkVDr1WX8
            return foo(aa, 26, closed, other_players - 1)
        else:
            return 0

    ps = 0

    # try to open
    if bit_test(closed, cur):
        r = rates[cur]
        p = (rem - 1) * r

        nc = bit_unset(closed, cur)

        ps = max(ps, p + foo(cur, rem-1, nc))

    # try each child
    for c, dist in d[cur]:
        ps = max(ps, foo(c, rem-dist, closed, other_players))

    return ps

closed = reduce(bit_set, closed, 0)

# part 1
print(foo(aa, 30, closed, 0))

# part 2
print(foo(aa, 26, closed, 1))