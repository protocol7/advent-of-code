import sys
from collections import defaultdict
from util import ints

def parse(line):
    l = line.strip()
    a, b = l.split(":")
    b, c = b.split("|")
    a = ints(a)[0]

    return a, set(ints(b)), set(ints(c))


xs = list(map(parse, sys.stdin))

t = defaultdict(lambda: 1)
for a, b, c in xs:
    for i in range(a+1, a+1+len(b & c)):
        t[i] += t[a]

print(sum(t.values()))
