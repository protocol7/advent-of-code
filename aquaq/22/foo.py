import sys
from collections import *
from itertools import *
from util import *

def parse(line):
    return line.strip()

xs = ints(sys.stdin.read())

def to_roman(d):
    def c(n, low, mid, high):
        if n < 4:
            return low * n
        elif n == 4:
            return low + mid
        elif n == 5:
            return mid
        elif n == 9:
            return low + high
        else:
            return mid + low * (n - 5)

    r = c(d // 1000, "M", None, None)
    d %= 1000

    r += c(d // 100, "C", "D", "M")
    d %= 100

    r += c(d // 10, "X", "L", "C")
    d %= 10

    r += c(d, "I", "V", "X")

    return r

def ceasar(s):
    return ord(s) - ord("A") + 1

s = 0
for x in xs:
    s += sum(ceasar(a) for a in to_roman(x))

print(s)
