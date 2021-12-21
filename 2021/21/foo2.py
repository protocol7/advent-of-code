import sys
from functools import cache

def parse(line):
    return int(line.split()[-1])

D = (1, 2, 3)

@cache
def turn(p1, p2, s1, s2):
    w1 = 0
    w2 = 0

    for d1 in D:
        for d2 in D:
            for d3 in D:
                np1 = p1 + d1 + d2 + d3

                np1 = (np1 - 1) % 10 + 1

                ns1 = np1 + s1

                if ns1 >= 21:
                    w1 += 1
                else:
                    nw2, nw1 = turn(p2, np1, s2, ns1)
                    w1 += nw1
                    w2 += nw2
    
    return w1, w2

p1, p2 = map(parse, sys.stdin)

print(max(turn(p1, p2, 0, 0)))