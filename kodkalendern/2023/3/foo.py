import sys

def parse(line):
    return int(line.strip())

xs = list(map(parse, sys.stdin))

m = sum(xs) / len(xs)

print(sum(1 for _ in filter(lambda x: x == m, xs)))
