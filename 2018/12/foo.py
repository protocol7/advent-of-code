import sys
from collections import defaultdict, Counter

def flatmap(f, items):
    return chain.from_iterable(imap(f, items))

def parse(line):
    x, _, y = line.split()
    return x, y

inp = list(sys.stdin)

initial = inp[0].split()[2]

lines = map(parse, inp[2:])
patterns = defaultdict(lambda: ".")
for l1, l2 in lines:
    patterns[l1] = l2


pots = defaultdict(lambda: ".")

for i, p in enumerate(initial):
    pots[i] = p

for gen in range(20):
    start = min(pots.keys()) - 2
    end = max(pots.keys()) + 2
    new_pots = defaultdict(lambda: ".")
    for p in range(start, end):
        pat = pots[p-2] + pots[p-1] + pots[p] + pots[p+1] + pots[p+2]
        new_pots[p] = patterns[pat]
    s = ""
    for p in range(start, end):
        s += new_pots[p]
    pots = new_pots

c = 0
for k, v in pots.iteritems():
    if v == "#":
        c += k
print(c)
