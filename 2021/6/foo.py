import sys
from collections import *
from itertools import *
from util import *

xs = ints(sys.stdin.read())

for _ in range(80):
    ns = []

    for x in xs:
        if x == 0:
            ns.append(6)
            ns.append(8)
        else:
            ns.append(x - 1)

    xs = ns

print(len(xs))