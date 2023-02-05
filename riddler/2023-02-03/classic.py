from itertools import count
from random import random

def run(n, p):
    i = n
    k = 0

    while i > 0:
        k += 1
        if random() <= p:
            i = 99
        else:
            i -= 1

    return k

s = 0
for c in count(1):
    s += run(99, 0.01)

    print(s / c)