import sys

def parse(line):
    return [int(i) for i in line.strip().split("x")]

parsed = map(parse, sys.stdin)

def paper((l, w, h)):
    s1 = l * w
    s2 = w * h
    s3 = l * h

    return 2*s1 + 2*s2 + 2* s3 + min([s1, s2, s3])

print(sum(map(paper, parsed)))
