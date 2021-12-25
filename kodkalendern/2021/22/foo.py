import sys

for x in sys.stdin.read().split("\n"):
    if any(int(a) % 2 != int(b) % 2 for a, b in zip(x[::2], x[1::2])):
        print(x)

