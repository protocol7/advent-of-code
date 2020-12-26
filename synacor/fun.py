import sys
sys.setrecursionlimit(15000)
from functools import cache

# this script doesn't work as it runs out of recursion depth, see fun.rs instead

@cache
def fun(a, b, c):
    print(a, b, c)

    if a == 0:
        return b + 1
    else:
        if b == 0:
            return fun(a - 1, c, c)
        else:
            x = fun(a, b - 1, c)
            return fun(a - 1, x, c)


a = 4
b = 1
c = 4

x = fun(a, b, c)

print(x)