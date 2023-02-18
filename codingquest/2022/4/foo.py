import sys
from collections import Counter
from itertools import cycle
from util import *

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

def won(s):
    if "1111" in s:
        return 1
    elif "2222" in s:
        return 2
    elif "3333" in s:
        return 3

def won_col(bs):
    for c in bs:
        c = join(map(str, c))

        winner = won(c)
        if winner:
            return winner


def won_row(bs):
    for i in range(7):
        s = ""
        for c in bs:
            if len(c) > i:
                s += str(c[i])
            else:
                s += "0"

        winner = won(s)
        if winner:
            return winner

def won_pos_diag(bs):
    for c in range(-7, 7):
        s = ""
        for cc, r in zip(range(c, c+8), range(7)):
            if cc < 0 or cc >= len(bs):
                s += "0"
            else:
                col = bs[cc]
                if len(col) > r:
                    s += str(col[r])
                else:
                    s += "0"

        winner = won(s)
        if winner:
            return winner

def won_neg_diag(bs):
    for c in range(-7, 7):
        s = ""
        for cc, r in zip(range(c, c+8), range(6, -1, -1)):
            if cc < 0 or cc >= len(bs):
                s += "0"
            else:
                col = bs[cc]
                if len(col) > r:
                    s += str(col[r])
                else:
                    s += "0"

        winner = won(s)
        if winner:
            return winner

wins = Counter()
for x in xs:
    bs = [[], [], [], [], [], [], []]
    ps = cycle([1, 2, 3])

    for p, c in zip(ps, x):
        c = int(c)

        bs[c - 1].append(p)

        # won?
        winner = won_row(bs) or won_col(bs) or won_pos_diag(bs) or won_neg_diag(bs)
        if winner:
            wins[winner] += 1
            break

print(prod(wins.values()))
