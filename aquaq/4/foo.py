import sys
from math import sqrt

def parse(line):
    return line.strip()

xs = int(sys.stdin.read())

def factors(n):
    j = 2
    while n > 1:
        for i in range(j, int(sqrt(n+0.05)) + 1):
            if n % i == 0:
                n //= i ; j = i
                yield i
                break
        else:
            if n > 1:
                yield n; break

def coprime(a, b):
    a = set(factors(a))

    return not a & b

b = set(factors(xs))

cp = []
for i in range(1, xs):
    if coprime(i, b):
        cp.append(i)

print(sum(cp))
