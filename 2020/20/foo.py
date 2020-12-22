import sys
from util import *

xs = sys.stdin.read().split("\n\n")

trans = dict()
for x in xs:
    x = x.split()
    a = int(x[1][:-1])
    trans[a] = list(transpositions(x[2:]))

p = 1
# check each tile for how many edges it matches with other tiles
for k, v in trans.items():
    c = 0
    for t in v:
        for kk, vv in trans.items():
            if k == kk:
                continue

            for tt in vv:
                # check if top edge is same
                if t[0] == tt[0]:
                    c += 1

    # corners will match two other tiles, in two mirrors each
    if c == 4:
        p *= k

print(p)