import sys
from collections import *
from itertools import *
from util import *

cups = list(map(int, "942387615"))

def pickup(ps, cur):
    xs = []
    for _ in range(3):
        cur = ps[cur] # pick next
        xs.append(cur)
    return xs

def run(cups, turns):
    l = len(cups)

    ps = dict() # dict of pointer from number -> next
    for i in range(len(cups)):
        ps[cups[i]] = cups[(i+1) % l] # mod to get pointer from last to first

    mi = min(cups)
    ma = max(cups)

    cur = cups[0]

    for _ in range(turns):
        pick = pickup(ps, cur)

        n = cur - 1
        if n < mi:
            n = ma

        while n in pick:
            n -= 1
            if n < mi:
                n = ma

        ps[cur] = ps[pick[-1]] # current should point to after the picked up cups
        ps[pick[-1]] = ps[n] # end of the picked up cups should point to after the destination
        ps[n] = pick[0] # the destination should point to the first of the picked up cups

        cur = ps[cur] # now current is whatever is after current

    return ps

t1 = run(cups, 100)

cur = t1[1]
s = ""
while cur != 1:
    s += str(cur)
    cur = t1[cur]


print(s)

cups = cups + list(range(len(cups) +1, 1000000 + 1))

t2 = run(cups, 10_000_000)

print(t2[1] * t2[t2[1]])