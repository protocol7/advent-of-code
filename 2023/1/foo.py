import sys

t = 0
for x in sys.stdin.readlines():
    x = list(filter(lambda c: c.isdigit(), x))

    t += int(x[0] + x[-1])

print(t)
