import sys
from util import *

def parse(line):
    return ints(line.strip())

a, b = sys.stdin.read().split("\n\n")

a = list(map(parse, a.split("\n")))

def bb(line):
    x, y = line.strip().split(" ")[2].split("=")
    return x, int(y)

b = list(map(bb, b.strip().split("\n")))

def fold(xs, a):
    for dim, d in xs:

        def fold(x, y):
            if dim == "x":
                if x > d:
                    x = 2 * d - x
            elif dim == "y":
                if y > d:
                    y = 2 * d - y
            return x, y

        a = set([fold(x, y) for x, y in a])
    
    return a

print(len(fold(b[:1], a)))

print("")

aa = fold(b, a)

for y in range(max(y for _, y in aa) + 1):
    line = ""
    for x in range(max(x for x, _ in aa) + 1):
        line += "#" if (x, y) in aa else " "
    print(line)
