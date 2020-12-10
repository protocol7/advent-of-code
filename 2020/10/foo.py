import sys

def parse(line):
    return int(line.strip())

xs = sorted(list(map(parse, sys.stdin)))

xs = [0] + xs + [max(xs)+3]

d1 = 0
d3 = 0

for a, b in zip(xs, xs[1:]):
    d = b - a

    if d == 1:
        d1 += 1
    elif d == 3:
        d3 += 1

print(d1*d3)