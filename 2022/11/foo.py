import sys
from collections import Counter
from util import ints
from dataclasses import dataclass
from typing import List
from copy import deepcopy

def parse(line):
    return line.strip()

xs = sys.stdin.read().split("\n\n")

@dataclass
class Monkey:
    items: List[int]
    op: str
    m: str
    test: int
    iftrue: int
    iffalse: int

monkeys = []
lcm = 1
for x in xs:
    x = x.split("\n")
    items = ints(x[1])

    op = x[2].split()[-2]
    m = x[2].split()[-1]

    test = ints(x[3])[0]

    lcm *= test

    iftrue = ints(x[4])[0]
    iffalse = ints(x[5])[0]

    monkeys.append(Monkey(items, op, m, test, iftrue, iffalse))

for part2, rounds in ((False, 20), (True, 10000)):

    ms = deepcopy(monkeys)

    cs = Counter()
    for r in range(rounds):
        for mi, monkey in enumerate(ms):
            for wl in monkey.items:
                cs[mi] += 1

                if monkey.op == "*":
                    if monkey.m.isnumeric():
                        wl = wl * int(monkey.m)
                    else:
                        wl = wl * wl
                else:
                    wl = wl + int(monkey.m)

                if part2:
                    wl %= lcm
                else:
                    wl = wl // 3
                
                om  = monkey.iftrue if wl % monkey.test == 0 else monkey.iffalse

                ms[om].items.append(wl)

            monkey.items = []

    a, b = cs.most_common(2)

    print(a[1] * b[1])