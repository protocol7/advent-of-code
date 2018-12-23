import sys

def parse(line):
    return [int(i) for i in line.strip().split("x")]

parsed = map(parse, sys.stdin)

def ribbon((l, w, h)):
    s = sorted([l, w, h])
    return s[0] * 2 + s[1] * 2 + l * w * h

print(sum(map(ribbon, parsed)))
