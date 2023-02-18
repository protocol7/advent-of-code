import sys

def parse(line):
    return int(line.strip())

xs = list(map(parse, sys.stdin))

c = 0
for i in range(60, len(xs)):
    ra = sum(xs[i-60:i]) / 60

    if ra < 1500 or ra > 1600:
        c += 1

print(c)