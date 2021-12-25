import sys

for x in sys.stdin.read().split("\n"):
    if not any(c != x[-i] for i, c in enumerate(x, 1)):
        print(x)