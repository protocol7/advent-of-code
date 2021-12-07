import sys
from util import *

xs = ints(sys.stdin.read())

def minimize(cost):
    ms = sys.maxsize

    for x in range(min(xs), max(xs) + 1):
        s = cost(x)

        ms = min(ms, s)
    
    return ms

print(minimize(lambda x: sum(abs(x - d) for d in xs)))
print(minimize(lambda x: sum(abs(x - d) * (abs(x - d) + 1) // 2 for d in xs)))