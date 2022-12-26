import sys
from collections import *
from itertools import *
from util import *

def parse(line):
    line = line.strip()
    if line == "date,milk,cereal":
        return
    _, m, c = line.split(",")

    return int(m), int(c)

xs = list(map(parse, sys.stdin))
xs = xs[1:]

def fresh_milk(milk):
    return sum(x for x, exp in milk if exp >= turn)

milk = []
cereal = 0
for turn, (m, c) in enumerate(xs):
    # buy cereal
    cereal += c

    # eat breakfast
    if cereal >= 100 and fresh_milk(milk) >= 100:
        cereal -= 100

        to_drink = 100
        while to_drink > 0:
            mm, exp = milk.pop(0)

            if exp < turn:
                continue

            if mm > to_drink:
                milk.insert(0, (mm-to_drink, exp))
                break
            else:
                to_drink -= mm

    # buy milk
    if m > 0:
        milk.append((m, turn+5))

print(fresh_milk(milk) + cereal)