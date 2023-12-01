import sys

xs = sys.stdin.readlines()

t = 0
for x in xs:
    x = list(filter(lambda c: c.isdigit(), x))

    t += int(x[0] + x[-1])

print(t)
