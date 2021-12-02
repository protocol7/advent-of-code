import sys

xs = list(map(int, sys.stdin))

print(sum(b>a for a, b in zip(xs, xs[1:])))
print(sum(b>a for a, b in zip(xs, xs[3:])))

