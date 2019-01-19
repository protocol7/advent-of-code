import sys
from math import sqrt

def cc(xs):
    return "".join(xs)

def flip(p):
    out = []
    for row in p:
        out.append(cc(reversed(row)))
    return tuple(out)

def rotate(p):
    out = []
    for x in range(len(p)):
        out.append(cc([r[x] for r in p]))
    return tuple(out)

def parse(line, patterns):
    pat, out = [tuple(i.split("/")) for i in line.strip().split(" => ")]
    for _ in range(4):
        patterns[pat] = out
        pat = flip(pat)
        patterns[pat] = out

        pat = rotate(pat)

def mutate(pat):
    size = int(sqrt(len(pat)))
    if size % 2 == 0:
        step = 2
    else:
        step = 3
    outsize = step + 1

    np = {}
    outy = 0
    for y in range(0, size, step):
        outx = 0
        for x in range(0, size, step):
            p = []
            for sy in range(step):
                pr = []
                for sx in range(step):
                    pr.append(pat[(x+sx, y+sy)])
                p.append("".join(pr))
            p = tuple(p)
            out = patterns[p]

            for sy, row in enumerate(out):
                for sx, c in enumerate(row):
                    np[(outx+sx, outy+sy)] = c
            outx += outsize
        outy += outsize
    return np

def count_on(pat):
    return len(filter(lambda c: c == "#", pat.values()))

rounds = int(sys.argv[1])

patterns = {}
for line in sys.stdin:
    parse(line, patterns)

pat = {}
for y, row in enumerate((".#.", "..#", "###")):
    for x, c in enumerate(row):
        pat[(x, y)] = c

for _ in range(rounds):
    pat = mutate(pat)

print(count_on(pat))
