import sys
from collections import defaultdict
from itertools import chain, imap

def flatmap(f, items):
    return chain.from_iterable(imap(f, items))

def parse(line):
    pass

inp = sys.stdin.read().strip()

floor = 0

for i, c in enumerate(inp):
    if c == "(":
        floor += 1
    else:
        floor -= 1

    if floor < 0:
        print(i + 1)
        break
