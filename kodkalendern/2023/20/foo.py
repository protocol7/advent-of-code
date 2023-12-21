import sys

def parse(line):
    return int(line.strip())

xs = list(map(parse, sys.stdin))

t = 0
seq = 1
growing = True
for a, b in zip(xs, xs[1:]):
    if b > a:
        if growing:
            seq += 1
        else:
            t += seq
            growing = True
            seq = 2
    elif a > b:
        if not growing:
            seq += 1
        else:
            t += seq
            growing = False
            seq = 2

t += seq

print(t)
