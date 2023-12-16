import sys
from util import ints
from functools import cache


def parse(line):
    a, b = line.strip().split()
    return a, ints(b)


xs = list(map(parse, sys.stdin))

def validate(ss, gs):
    cc = []
    cont = 0
    for c in ss:
        if c == "#":
            cont += 1
        elif cont > 0:
            cc.append(cont)
            cont = 0
    
    if cont > 0:
        cc.append(cont)

    return cc == gs


def foo(ss, gs, valid):
    if "?" not in ss:
        if validate(ss, gs):
            valid.append(ss)
    else:
        for r in "#.":
            nss = ss.replace("?", r, 1)

            foo(nss, gs, valid)

t = 0
for ss, gs in xs:
    valid = []
    foo(ss, gs, valid)

    t += len(valid)

print(t)
