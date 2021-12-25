import sys

s = {}
for x in sys.stdin.read().split("\n"):
    f = frozenset(x)

    if f in s:
        print(x, s[f])
        break
    s[f] = x
