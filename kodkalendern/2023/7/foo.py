import sys
from collections import Counter


def parse(line):
    return int(line.strip().split(", ")[1])


c = Counter(map(parse, sys.stdin))

print(c.most_common(1)[0][0])

