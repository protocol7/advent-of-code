import sys
from util import *

def parse(line):
    return ints(line.strip())

xs = list(map(parse, sys.stdin))

s = 0
for x in xs:
    for i in range(len(x)):
        streaks = set()

        for start in range(i+1):
            for end in range(i+1, len(x)+1):
                sub = x[start:end]

                # if comfortable?
                if sum(sub) % len(sub) == 0:
                    streaks.add(len(sub))

        streaks = sorted(streaks)

        length = len(streaks)
        for i in range(len(streaks)):
            if streaks[i] - 1 != i:
                length = i
                break

        s += length

print(s)
