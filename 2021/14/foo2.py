import sys
from collections import *

def parse(line):
    return line.strip().split(" -> ")

a, b = sys.stdin.read().split("\n\n")

a = a.strip()

b = list(map(parse, b.strip().split("\n")))

b = {k: v for k, v in b}

# dict of pair -> count
p = defaultdict(int)
for x, y in zip(a, a[1:]):
    p[x+y] += 1

for _ in range(40):
    pp = defaultdict(int)

    for x, y in p.items():
        g = b[x]

        pp[x[0] + g] += y
        pp[g + x[1]] += y

    p = pp

c = Counter()

for k, v in p.items():
    c[k[0]] += v

c[a[-1]] += 1

cc = c.most_common()

print(cc[0][1] - cc[-1][1])