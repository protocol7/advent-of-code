import sys

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

t = 0
for x in xs:
    for i in range(1, len(x) + 1):
        if len(x) % i != 0:
            continue

        p = x[:i]
        m = len(x) // len(p)

        if p * m == x:
            t += m
            break

print(t)
