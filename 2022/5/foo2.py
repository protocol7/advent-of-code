import sys
from util import *

def parse(line):
    return ints(line.strip())

a, b = sys.stdin.read().strip().split("\n\n")

a = a.split("\n")

cols = []
for i in range(1, len(a[0]), 4):
    cols.append([r[i] for r in a if r[i] != " "][:-1])

b = list(map(parse, b.split("\n")))

for n, fr, to in b:
    l = []
    for _ in range(n):
        x = cols[fr-1].pop(0)

        l.insert(0, x)

    for x in l:
        cols[to-1].insert(0, x)

print(join(col[0] for col in cols))