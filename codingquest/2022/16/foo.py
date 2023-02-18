import sys

def parse(line):
    return [int(x, 16) for x in line.split()]

xs = list(map(parse, sys.stdin))

ccs = xs[-1]
cs = xs[:-1]

y = None
for i, row in enumerate(cs):
    expected = row[-1]
    row = row[:-1]

    actual = sum(row) % 256

    if actual != expected:
        delta = (actual - expected) % 256
        y = i
        break

x = None
for i, expected in zip(range(len(xs[0]) - 1), ccs):
    actual = sum(cc[i] for cc in cs) % 256

    if expected != actual:
        x = i
        break

print(cs[y][x] * (cs[y][x] - delta))
