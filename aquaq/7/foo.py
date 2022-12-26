import sys
from collections import *
from itertools import *
from util import *

def parse(line):
    line = line.strip()
    if line == "h,a,score":
        return None
    a, b, c =  line.split(",")
    c, d = map(int, c.split("-"))

    return a, b, c, d

xs = list(map(parse, sys.stdin))

xs = xs[1:]

players = set(x[0] for x in xs) | set(x[1] for x in xs)

# give each a rating of 1200
players = {p: 1200 for p in players}

for a, b, c, d in xs:
    Ra = players[a]
    Rb = players[b]

    Ea = 1 / (1 + pow(10, ((Rb-Ra)/400)))
    Eb = 1 / (1 + pow(10, ((Ra-Rb)/400)))

    if c > d:
        # player a wins
        Rap = Ra + 20 * (1-Ea)
        Rbp = Rb - 20 * (1-Ea)
    else:
        Rap = Ra - 20 * (1-Eb)
        Rbp = Rb + 20 * (1-Eb)

    players[a] = Rap
    players[b] = Rbp

a = int(min(players.values()))
b = int(max(players.values()))

print(b - a)