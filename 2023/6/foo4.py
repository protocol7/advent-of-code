import sys
from util import ints, binary_search


def parse(line):
    return ints(line.strip())


xs = list(map(parse, sys.stdin))

a = int("".join(str(x) for x in xs[0]))
b = int("".join(str(x) for x in xs[1]))

def ternary_search(f, left, right, absolute_precision) -> float:
    """Find maximum of unimodal function f() within [left, right].
    To find the minimum, reverse the if/else statement or reverse the comparison.
    """
    while abs(right - left) >= absolute_precision:
        left_third = left + (right - left) / 3
        right_third = right - (right - left) / 3

        if f(left_third) < f(right_third):
            left = left_third
        else:
            right = right_third

    # Left and right are the current bounds; the maximum is between them
    return (left + right) / 2

def d(i):
    return i * (a - i)

# don't guess, find the maxmimum point
ma = int(ternary_search(d, 0, a, 1))

_, f = binary_search(0, ma, lambda i: d(i) > b)
_, g = binary_search(ma, a, lambda i: d(i) < b)

print(g - f)
