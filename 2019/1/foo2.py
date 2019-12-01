import sys

def f(i):
    s = 0
    f = int(i) / 3 - 2
    while f > 0:
        s += f
        f = f / 3 - 2
    return s

print(sum(map(f, sys.stdin)))
