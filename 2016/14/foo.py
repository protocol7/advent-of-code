import sys
from collections import defaultdict
from itertools import count
import hashlib
import re


def triplet(s):
    m = re.search(r"([a-z0-9])\1\1", s)
    if m:
        return m.group(1)

def fives(s):
    m = re.search(r"([a-z0-9])\1\1\1\1", s)
    if m:
        return m.group(1)

def keys(s, hash):
    open = defaultdict(list)
    matches = []
    for i in count():
        h = hash(s + str(i))

        five = fives(h)
        if five and five in open:
            for index in open[five]:
                if i - index <= 1000:
                    matches.append(index)
                    open[five] = [] # why?

                    # we're looking for the 64th index, not the 64 match, so we go a
                    # bit extra, and then pick the 64th
                    if len(matches) >= 64 and i > matches[63] + 1000:
                        matches.sort()
                        return matches[63]

        t = triplet(h)
        if t:
            open[t].append(i)

def part2(s):
    for _ in range(2017):
        s = hashlib.md5(s).hexdigest()
    return s

inp = sys.argv[1].strip()

print(keys(inp, lambda s: hashlib.md5(s).hexdigest()))
print(keys(inp, part2))
