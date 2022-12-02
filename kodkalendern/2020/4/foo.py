import sys

def parse(line):
    return line.strip()

xs = sorted(map(parse, sys.stdin))

print(xs[475])