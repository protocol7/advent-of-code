import sys
from collections import defaultdict

def parse(line):
    l = line.split()
    return l[0], l[1], int(l[2]), l[4], l[5], int(l[6])

ins = map(parse, sys.stdin)

reg = defaultdict(int)

highest = -sys.maxint
for r, op, by, cr, cp, ci in ins:
    v = reg[cr]
    ok = False
    if cp == ">":
        ok = v > ci
    elif cp == "<":
        ok = v < ci
    elif cp == ">=":
        ok = v >= ci
    elif cp == "<=":
        ok = v <= ci
    elif cp == "==":
        ok = v == ci
    elif cp == "!=":
        ok = v != ci

    if ok:
        if op == "inc":
            reg[r] += by
        elif op == "dec":
            reg[r] -= by
    highest = max(highest, max(reg.values()))

print(max(reg.values()))
print(highest)
