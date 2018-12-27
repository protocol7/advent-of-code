import sys

def factor(n):
    factors = []
    i = 2
    x = n // i
    while i < x:
        if n % i == 0:
            factors.append(i)
            factors.append(n // i)
            x = n // i
        i += 1
    return [1] + factors + [n]

def val(i):
    f = set(factor(i))
    f = filter(lambda x: x * 50 >= i, f)
    return sum(f) * 11

# magic numbers derived through some binary searching
for i in range(700000, 800000):
    s = val(i)
    if s >= 29000000:
        print(i)
        break
