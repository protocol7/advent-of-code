import sys
from itertools import cycle
from util import msplit, equals
from math import lcm

def parse(line):
    x, y, z = msplit(line.strip(), " (,)]=")

    return x, (y, z)

a, b = sys.stdin.read().split("\n\n")

a = ["LR".index(x) for x in a]

bs = dict(map(parse, b.splitlines()))

def steps(cur, end):
    for s, d in enumerate(cycle(a), 1):
        cur = bs[cur][d]

        if end(cur):
            break

    return s

# part 1
print(steps("AAA", equals("ZZZ")))

# part 2
curs = [b for b in bs if b.endswith("A")]
p = [steps(cur, lambda c: c.endswith("Z")) for cur in curs]

print(lcm(*p))
