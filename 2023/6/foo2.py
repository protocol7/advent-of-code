import sys
from util import ints


def parse(line):
    return ints(line.strip())


xs = list(map(parse, sys.stdin))

a = int("".join(str(x) for x in xs[0]))
b = int("".join(str(x) for x in xs[1]))

print(a, b)
print(42826983 - 6960997)

w = 0
for i in range(a+1):
    d = i * (a - i)

    w += d > b

print(w)



