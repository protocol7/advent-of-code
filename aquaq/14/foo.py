import sys
from collections import *
from itertools import *
from util import *
from copy import deepcopy

def parse(line):
    return ints(line.strip())

xs = list(map(parse, sys.stdin))

board = [
    ints("6  17 34 50 68"),
    ints("10 21 45 53 66"),
    ints("5  25 36 52 69"),
    ints("14 30 33 54 63"),
    ints("15 23 41 51 62"),
]

bs = board + transpose(board)

d = []
for i in range(len(board)):
    d.append(board[i][i])
bs.append(d)

d = []
for i in range(len(board)):
    d.append(board[len(board) - i - 1][i])
bs.append(d)

def foo(x, b):
    for i, xx in enumerate(x):
        for bb in b:
            try:
                bb.remove(xx)

                if len(bb) == 0:
                    # bingo!
                    return i + 1

            except ValueError:
                pass

s = 0
for x in xs:
    b = deepcopy(bs)
    s += foo(x, b)

print(s)