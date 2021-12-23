import sys
from collections import *

def parse(line):
    return line.strip().split(" -> ")

a, b = sys.stdin.read().split("\n\n")

a = a.strip()

b = list(map(parse, b.strip().split("\n")))

b = {k: v for k, v in b}

for _ in range(10):
    a = "".join(x + b[x + y] for x, y in zip(a, a[1:])) + a[-1]

c = Counter(a)

cc = c.most_common()

print(cc[0][1] - cc[-1][1])