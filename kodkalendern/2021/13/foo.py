import sys

s = 0
for x in sys.stdin.read().split("\n"):
    valid = True
    for i, c in enumerate(x, 1):
        if i == int(c):
            valid = False

    s += valid

print(s)