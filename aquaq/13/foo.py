import sys
from collections import *
from itertools import *
from util import *

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

def num_repeats(s, ss):
    for r in count(1):
        if ss * r not in s:
            return r - 1

def substrings(s):
    out = []
    for start in range(len(s)):
        for end in range(start+1, len(s)+1):
            out.append(s[start:end])

    return out

s = 0
for x in xs:
    s += max(num_repeats(x, ss) for ss in substrings(x))

print(s)