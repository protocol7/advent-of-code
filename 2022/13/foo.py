import sys
from itertools import zip_longest
from util import *
from functools import cmp_to_key

def compare(a, b):
    if type(a) == int and type(b) == int:
        return sign(a - b)
    elif type(a) == list and type(b) == list:
        for aa, bb in zip_longest(a, b):
            if aa is None:
                return -1
            elif bb is None:
                return 1
            else:
                c = compare(aa, bb)
                if c != 0:
                    return c
        return 0
    elif type(a) == int:
        return compare([a], b)
    elif type(b) == int:
        return compare(a, [b])

xs = [eval(x) for x in sys.stdin if x.strip()]

# part 1
print(sum(i+1 for i, (a, b) in enumerate(chunks(xs, 2)) if compare(a, b) == -1))

# part 2
dividers = [[[6]], [[2]]]

xx = sorted(xs + dividers, key=cmp_to_key(compare))

print(product(i+1 for i, x in enumerate(xx) if x in dividers))