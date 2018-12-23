import sys
import re
from collections import defaultdict
from itertools import chain, imap

def flatmap(f, items):
    return chain.from_iterable(imap(f, items))

def parse(line):
    return [int(i) for i in re.findall("-?\d+", line)]

def overlap(bb):
    os = sorted([o for o, _ in bb])
    cs = sorted([o for _, o in bb])

    i = 0
    j = 0

    open = 0
    maxopen = -sys.maxint
    io = -sys.maxint
    ic = sys.maxint
    while i < len(os) and j < len(cs):
        o = os[i]
        c = cs[j]
        if o <= c:
            open += 1
            i += 1
        if open > maxopen:
            io = o
            ic = c
        maxopen = max(open, maxopen)
        if c <= o:
            open -= 1
            j += 1

    return io, ic

bots = map(parse, sys.stdin)

i = []
for x, y, z, r in bots:
    i.append(((x-r, x+r), (y-r, y+r), (z-r, z+r)))

xx = overlap([x for x, _, _ in i])
yy = overlap([x for _, x, _ in i])
zz = overlap([x for _, _, x in i])

def man_dist((x1, y1, z1), (x2, y2, z2)):
    return abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1)

most = -sys.maxint
most_coord = None
for x in range(xx[0], xx[1]+1):
    for y in range(yy[0], yy[1]+1):
        for z in range(zz[0], zz[1]+1):
            c = 0
            for bx, by, bz, br in bots:
                if man_dist((x, y, z), (bx, by, bz)) <= br:
                    c += 1
            if c > most:
                most = c
                most_coord = (x, y, z)
print(sum(most_coord))
