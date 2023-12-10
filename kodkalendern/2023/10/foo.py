import sys

def parse(line):
    return line.strip().rsplit(" ", 1)

xs = map(parse, sys.stdin)

for x, _ in xs:
    if len(x.replace(" ", "")) == 8:
        print(x)
