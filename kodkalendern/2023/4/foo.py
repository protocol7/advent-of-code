import sys

def parse(line):
    return int(line.strip())

xs = map(parse, sys.stdin)

print(min(xs, key=lambda x: abs(106023 - x)))
