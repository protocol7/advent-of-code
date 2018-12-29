import sys

lines = list(sys.stdin)

def parse(line):
    return [int(i) for i in line.split()]

ts = []
for i in range(0, len(lines), 3):
    l1, l2, l3 = [parse(line) for line in lines[i:i+3]]
    for t in zip(l1, l2, l3):
        ts.append(sorted(t))

valid = filter(lambda (s1, s2, s3): s1 + s2 > s3, ts)
print(len(valid))
