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

def cc(pots):
    c = 0
    for k, v in pots.iteritems():
        if v == "#":
            c += k
    return c

def debug(pots):
    s = ""
    start = min(pots.keys())
    end = max(pots.keys())
    for p in range(start, end):
        s += pots[p]
    return s


for gen in range(5000):
    start = min(pots.keys()) - 2
    end = max(pots.keys()) + 2
    new_pots = defaultdict(lambda: ".")
    for p in range(start, end):
        pat = pots[p-2] + pots[p-1] + pots[p] + pots[p+1] + pots[p+2]
        pot = patterns[pat]
        if pot == "#":
            new_pots[p] = pot

    s2 = debug(new_pots)
    s1 = debug(pots)

    print(str(gen) + "," + str(cc(new_pots)))
    pots = new_pots
