import sys

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

c = 0
for x in xs:
    c += x.count(".")

print(c)