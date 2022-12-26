import sys
from collections import *
from itertools import *
from util import *

def parse(line):
    return line.strip().split(",")

xs = list(map(parse, sys.stdin))

words = set()
letters = set()
with open("words.txt") as f:
    for word in f:
        word = word.strip()
        words.add(word)

        letters |= set(word)

s = 1
for a, b in xs:
    ws = set([a])

    turn = 0
    while b not in ws:
        nws = set()
        for w in ws:
            for i in range(len(w)):
                for c in letters:
                    nw = w[:i] + c + w[i+1:]
                    if nw in words:
                        nws.add(nw)

        ws = nws
        turn += 1

    s *= (turn+1)

print(s)