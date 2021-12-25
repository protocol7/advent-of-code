import sys

for x in sys.stdin.read().split("\n"):
    p0, p1, p2, p3, p4, p5 = map(int, x)

    if p0 + p5 < p1 + p4 < p2 + p3:
        print(x)