import sys
from collections import defaultdict

def filter_dict(d, fn):
    return {k: v for k, v in d.iteritems() if fn(k, v)}

inp = list(sys.stdin)

initial = inp[0].split()[2]
pots = defaultdict(lambda: ".")
for i, p in enumerate(initial):
    pots[i] = p

patterns = defaultdict(lambda: ".")
for line in inp[2:]:
    x, _, y = line.split()
    patterns[x] = y

for gen in range(20):
    start = min(pots.keys()) - 2
    end = max(pots.keys()) + 2
    new_pots = defaultdict(lambda: ".")
    for p in range(start, end):
        pat = pots[p-2] + pots[p-1] + pots[p] + pots[p+1] + pots[p+2]
        new_pots[p] = patterns[pat]
    pots = new_pots

print(sum(filter_dict(pots, lambda _, v: v == "#")))
