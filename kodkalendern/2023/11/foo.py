import sys
from collections import *
from itertools import *
from util import *


def parse(line):
    a, b, c = line.strip().split(", ")
    c = int(c)

    return b, c

KBD = "qwertyuiopåasdfghjklöäzxcvbnm"


xs = list(map(parse, sys.stdin))

t = 0
for b, c in xs:
    s = ""
    for x in b:
        i = KBD.index(x)

        i = (i - c) % len(KBD)

        s += KBD[i]

    t += s == "cykel"
        
print(t)
