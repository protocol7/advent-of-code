import sys
from collections import defaultdict
from math import prod
from util import Grid


g = Grid([l.strip() for l in sys.stdin.readlines()])

d = []
pos = []
ds = ""
lp = None
for p, c in g.points():
    # do we have a digit, and we're no longer in one, or at the end of a row?
    if ds and (not c.isdigit() or lp.y != p.y):
        d.append((ds, pos))
        ds = ""
        pos = []

    if c.isdigit():
        ds += c
        pos.append(p)

    lp = p

# part 1
t = 0
for ds, ps in d:
    ok = False
    for p in ps:
        for _, a in g.adjacent(p):
            if a is None or a.isdigit() or a == ".":
                continue
            else:
                ok = True

    if ok:
        t += int(ds)

print(t)

# part 2
gs = defaultdict(list)
for ds, ps in d:
    ok = set()
    for p in ps:
        for ap ,a in g.adjacent(p):
            if a == "*":
                ok.add(ap)

    for ap in ok:
        gs[ap].append(int(ds))


t = 0
for g in gs.values():
    if len(g) == 2:
        t += prod(g)

print(t)
