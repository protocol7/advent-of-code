import sys
from collections import *


def parse(line):
    return line.strip()

def gen_m():
    return ["....."] * 5

m = tuple(map(parse, sys.stdin))

ms = defaultdict(gen_m)
ms[0] = m

def pp(m):
    for line in m:
        print("".join(line))
    print("")

def ppp(ms):
    start = min(ms.keys())
    end = max(ms.keys())
    for i in range(start, end+1):
        print("Depth %s:" % i)
        pp(ms[i])

w = 5
h = 5

adjacent = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def tick(m, mu, md):
    mm = []
    for y, line in enumerate(m):
        ll = []
        for x, c in enumerate(line):
            n = 0
            for dx, dy in adjacent:
                ax = x + dx
                ay = y + dy

                if ax < 0:
                    cc = mu[2][1]
                elif ay < 0:
                    cc = mu[1][2]
                elif ax >= w:
                    cc = mu[2][3]
                elif ay >= h:
                    cc = mu[3][2]
                elif ax == 2 and ay == 2:
                    # handle down map
                    if x == 2 and y == 1:
                        # 8
                        cc = md[0]
                    elif x == 2 and y == 3:
                        cc = md[-1]
                    elif x == 1 and y == 2:
                        cc = [l[0] for l in md]
                    elif x == 3 and y == 2:
                        cc = [l[-1] for l in md]
                    else:
                        assert False
                else:
                    cc = m[ay][ax]

                n += cc.count("#")

            if x == 2 and y == 2:
                ll.append(".")
            elif c == "#":
                if  n == 1:
                    ll.append("#")
                else:
                    ll.append(".")
            elif c == ".":
                if  n == 1 or n == 2:
                    ll.append("#")
                else:
                    ll.append(".")
            else:
                assert False
        mm.append("".join(ll))
    return tuple(mm)

def ticks(ms):
    mss = defaultdict(gen_m)

    start = min(ms.keys()) - 1
    end = max(ms.keys()) + 1
    for i in range(start, end + 1):
        mu = ms[i-1]
        md = ms[i+1]

        mss[i] = tick(ms[i], mu, md)
    return mss

def bugs(ms):
    b = 0
    for m in ms.values():
        for l in m:
            b += l.count("#")
    return b

for gen in range(200):
    ms = ticks(ms)

print(bugs(ms))
