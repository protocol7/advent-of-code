from itertools import count
from random import random

def run(n, p):
    i = n
    k = 0

    while i > 0:
        k += 1
        if random() <= p:
            i = n
        else:
            i -= 1

    return k

def avg(n, p):
    ROUNDS = 10000
    s = 0
    for _ in range(ROUNDS):
        s += run(n, p)

    return s / ROUNDS

print(avg(1000, 1/1000) / 1000)
print(avg(10000, 1/10000) / 10000)
print(avg(100000, 1/100000) / 100000)

