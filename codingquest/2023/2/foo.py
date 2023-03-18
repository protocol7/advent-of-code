import sys
from util import *


def parse(line):
    return int(line.strip())

xs = list(map(parse, sys.stdin))

ps = []
for x in xs:
    b = binary(x, 16)

    if b.count("1") % 2 == 0:
        ps.append(int(b[1:], 2))

print(round(sum(ps) / len(ps)))