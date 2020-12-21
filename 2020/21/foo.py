import sys
from collections import *
from util import *

def parse(line):
    a, b = line.strip().split(" (contains ")

    return a.split(), b[:-1].split(", ")

xs = list(map(parse, sys.stdin))

# dict of allergen to sets of possible foods
d = defaultdict(list)
for a, b in xs:
    for x in b:
        d[x].append(set(a))

# for each allergen, find the foods that exists in all lists of possible foods
rem = dict()
for k, v in d.items():
    rem[k] = set.intersection(*v)

# reduce down to the unique options
unique = reduce_unique_options(rem)
foods = set(unique.values())

print(sum(len(set(x) - foods) for x, _ in xs))

print(",".join(x for _, x in sorted(unique.items())))