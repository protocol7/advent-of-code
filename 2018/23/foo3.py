import sys
import re
from collections import defaultdict
from itertools import chain, imap

def flatmap(f, items):
    return chain.from_iterable(imap(f, items))

def parse(line):
    return [int(i) for i in re.findall("-?\d+", line)]

def man_dist(x1, y1, z1, x2, y2, z2):
    return abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1)

def in_range((x1, y1, z1, r1), (x2, y2, z2, r2)):
    return man_dist(x1, y1, z1, x2, y2, z2) <= (r1 + r2)

def new_cands(x, y, z, r):
    return [(x + sx * r, y + sy * r, z + sz * r) for sx in [-1, 0, 1] for sy in [-1, 0, 1] for sz in [-1, 0, 1]]

bots = map(parse, sys.stdin)

# seed with candidates
cands = [(x, y, z) for x, y , z, _ in bots]

# pick a reasonable starting span, doesn't seem to matter very much
xs = [x for x, _, _, _ in bots]
ys = [x for _, x, _, _ in bots]
zs = [x for _, _, x, _ in bots]

xspan = max(xs) - min(xs)
yspan = max(ys) - min(ys)
zspan = max(zs) - min(zs)

span = max([xspan, yspan, zspan])

while span > 0:
    span = span // 2
    cands = flatmap(lambda (x, y, z): new_cands(x, y, z, span), cands)

    # count to set of candidates, to be able to pick the set of candidates with
    # most matches
    count_cand = defaultdict(set)
    for cx, cy, cz in cands:
        count = 0
        for bx, by, bz, br in bots:
            if in_range((cx, cy, cz, span), (bx, by, bz, br)):
                count += 1
        count_cand[count].add((cx, cy, cz))

    m = max(count_cand.keys())
    cands = set(count_cand[m])

(cands,) = cands
print(sum(cands))
