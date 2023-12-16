import sys
from collections import Counter

def parse(line):
    return line.strip()

def norm(s):
    return "".join(x for x in s if not x.isdigit())


xs = list(map(parse, sys.stdin))
c = Counter(norm(x) for x in xs)

for a, b in c.items():
    if b == 1:
        for x in xs:
            if norm(x) == a:
                print(x)
