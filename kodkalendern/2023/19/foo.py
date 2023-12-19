import sys

def parse(line):
    return line.strip().split(", ")

xs = list(map(parse, sys.stdin))

w = 0
for a, b, c, d, e, f, g, h, i in xs:
    if a <= b <= c and d <= e <= f and g <= h <= i and a <= d <= g:
        continue
    else:
        w += 1

print(w)
