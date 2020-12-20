import sys
from collections import *
from itertools import *
from util import *

xs = sys.stdin.read().split("\n\n")

d = dict()

for x in xs:
    x = x.split()

    a = int(x[1][:-1])

    b = x[2:]

    d[a] = b

def edge(x):
    es = []

    # top
    es.append(x[0])
    es.append("".join(reversed(x[0])))

    # bottom
    es.append(x[-1])
    es.append("".join(reversed(x[-1])))

    # left
    s = ""
    for xx in x:
        s += xx[0]
    es.append(s)
    es.append("".join(reversed(s)))

    # right
    s = ""
    for xx in x:
        s += xx[-1]
    es.append(s)
    es.append("".join(reversed(s)))

    return es

edges = dict()
for k, v in d.items():
    e = edge(v)
    edges[k] = e

    print(e)

p = 1

for k, v in edges.items():

    ms = 0
    for e in v:
        for kk, vv in edges.items():
            if k == kk:
                continue

            for ee in vv:
                if e == ee:
                    # print(e, ee, k, kk)
                    ms += 1

    if ms == 4:
        p *= k

print(p)