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
    for _ in range(n):
        cols[to-1].insert(0, cols[fr-1].pop(0))

print(join(col[0] for col in cols))