import sys
from itertools import *

def parse(line):
    return int(line.strip())

xs = list(map(parse, sys.stdin))

p = int(sys.argv[1])

def m(pre, x):
    for a, b in product(pre, pre):
        if a == b:
            continue

        if a + b == x:
            return True

# find first that doesn't have a preceeding sum
def find_first():
    for i in range(p, len(xs)):
        pre = xs[i-p:i]
        x = xs[i]

        if not m(pre, x):
            return x


def find_sum_min_max(x):
    for i in range(len(xs)):
        for j in range(i, len(xs)):
            s = xs[i:j]
            ss = sum(s)

            if ss == x:
                return (min(s) + max(s))
            elif ss > x:
                break

first = find_first()
print(first)
print(find_sum_min_max(first))