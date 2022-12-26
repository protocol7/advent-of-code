import sys
from functools import cache

target = int(sys.stdin.read().strip())

darts = list(range(1, 21))
darts += [2 * x for x in darts] + [3 * x for x in darts]
darts += [25, 50]
darts = list(reversed(sorted(set(darts))))

@cache
def foo(n):
    # how minimum many darts do you need to reach zero from n
    
    if n == 0:
        return 0

    if n < 0:
        return -1

    m = sys.maxsize
    for dart in darts:
        d = foo(n - dart)

        if d != -1:
            m = min(m, d)

    if m == sys.maxsize:
        return -1
    else:
        return 1 + m

print(sum(foo(i) for i in range(target+1)))
