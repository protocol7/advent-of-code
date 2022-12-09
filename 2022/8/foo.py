import sys
from util import *
from itertools import takewhile

def parse(line):
    return list(map(int, line.strip()))

xs = list(map(parse, sys.stdin))

w = len(xs[0])
h = len(xs)

ss = set()
for y, row in enumerate(xs):
    m = -1
    for x, c in enumerate(row):
        if c > m:
            ss.add((x, y))
            m = c
    
    m = -1
    for x, c in enumerate(row[::-1]):
        if c > m:
            ss.add((w-x-1, y))
            m = c

for y, row in enumerate(transpose(xs)):
    m = -1
    for x, c in enumerate(row):
        if c > m:
            ss.add((y, x))
            m = c
    
    m = -1
    for x, c in enumerate(row[::-1]):
        if c > m:
            ss.add((y, w-x-1))
            m = c

print(len(ss))