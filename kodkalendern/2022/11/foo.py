import sys

def parse(line):
    return line.strip().split(", ")

xs = list(map(parse, sys.stdin))

h = 0
for x in xs:
    for a, b in zip(*x):
        h += a != b

print(h)