import sys
from itertools import chain

def parse(line):
    ls = line.split()
    ls.pop(1)
    return set([int(i.strip(",")) for i in ls])

parsed = map(parse, sys.stdin)

groups = []
for p in parsed:
    overlapping = filter(lambda g: g.intersection(p), groups)
    nonmatching = [g for g in groups if g not in overlapping]

    if not overlapping:
        # there are no overlapping groups, create a new
        groups = [p] + nonmatching
    else:
        s = set(chain(*overlapping))
        s.update(p)
        groups = [s] + nonmatching

for g in groups:
    if 0 in g:
        print(len(g))

print(len(groups))
