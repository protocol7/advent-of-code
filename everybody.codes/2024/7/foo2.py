#!/usr/bin/env python3

import sys
from collections import *
from itertools import *
from util import *


def parse(line):
    a, b = line.strip().split(":")
    return a, b.split(",")


xs = list(map(parse, sys.stdin))

track = "-=++=-==++=++=-=+=-=+=+=--=-=++=-==++=-+=-=+=-=+=+=++=-+==++=++=-=-=---=++==--+++==++=+=--==++==+++=++=+++=--=+=-=+=-+=-+=-+-=+=-=+=-+++=+==++++==---=+=+=-S"


out = []
for a, bs in xs:
    p = 10
    s = 0

    bs = cycle(bs)

    for loop in range(10):
        for t, b in zip(track, bs):
            if t == "=" or t == "S":
                if b == "=":
                    pass
                elif b == "+":
                    p += 1
                elif b == "-" and p > 0:
                    p -= 1
                else:
                    assert False
            elif t == "+":
                p += 1
            elif t == "-" and p > 0:
                p -= 1
            else:
                assert False

            s += p

    out.append((a, s))

out = sorted(out, key=lambda x: x[1], reverse=True)
print("".join(x[0] for x in out))
