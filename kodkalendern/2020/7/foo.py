import sys

xs = sys.stdin.read()

s = int(xs[0])

for i, x in enumerate(xs[1:]):
    x = int(x)

    if i % 2 == 0:
        s += x
    else:
        s -= x

print(s)