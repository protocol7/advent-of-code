import sys

xs = sys.stdin.read().strip()

i = 0

while True:
    x = int(xs[i])

    if x == 0:
        print(i)
        break

    i += x
