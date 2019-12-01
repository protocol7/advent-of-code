import sys

def f(i):
    return int(i) / 3 - 2

print(sum(map(f, sys.stdin)))
