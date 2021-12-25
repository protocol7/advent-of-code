import sys
from functools import reduce

def f(a, b):
    _, a = a
    i, b = b

    if i % 3 == 1:
        return 0, a + b
    elif i % 3 == 2:
        return 0, a * b
    elif i % 3 == 0:
        return 0, a - b

print(reduce(f, enumerate(map(int, sys.stdin)))[1])