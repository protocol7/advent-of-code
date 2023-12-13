import sys
from util import transpose

def parse(line):
    return line.strip()

xs = [list(map(parse, x.splitlines())) for x in sys.stdin.read().split("\n\n")]

def mirror(x, i):
    return x[:i][::-1], x[i:]

def count_errors(x, i):
    a, b = mirror(x, i)

    # valid mirror planes must have at least one row
    if not a or not b:
        return -1

    # count the number of non-matching in each row in each of the two mirror planes
    return sum(ca != cb for aa, bb in zip(a, b) for ca, cb in zip(aa, bb))

def check(x, expected):
    def foo(x):
        for i in range(len(x)+1):
            if count_errors(x, i) == expected:
                return i
            
        return 0

    return foo(x) * 100 + foo(transpose(x))


for expected in (0, 1):
    print(sum(check(x, expected) for x in xs))
