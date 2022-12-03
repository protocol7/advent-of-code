import sys

def parse(line):
    return int(line.strip())

xs = list(map(parse, sys.stdin))

for i, x in enumerate(xs):
    if x == 83 * 60 * 24:
        print(i+1)
        break