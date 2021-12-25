import sys
from collections import Counter
from math import prod

c = Counter()
for x in sys.stdin.read().split("\n"):
    c[prod(map(int, x))] += 1

print(c.most_common(1)[0][0])
