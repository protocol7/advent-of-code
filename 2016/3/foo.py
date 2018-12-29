import sys

def parse(line):
    return sorted([int(i) for i in line.split()])

ts = map(parse, sys.stdin)

valid = filter(lambda (s1, s2, s3): s1 + s2 > s3, ts)
print(len(valid))
