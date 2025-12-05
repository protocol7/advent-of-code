#!/usr/bin/env python3

import sys

def parse_a(line):
    return list(map(int, line.strip().split("-")))

a, b = sys.stdin.read().strip().split("\n\n")

rs = list(map(parse_a, a.split("\n")))

t = 0
for bb in b.split("\n"):
    bb = int(bb)

    for mi, ma in rs:
        if bb >= mi and bb <= ma:
            t += 1
            break

print(t)
