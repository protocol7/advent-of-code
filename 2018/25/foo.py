import sys

def parse(line):
    return tuple([int(i) for i in line.split(",")])

def man_dist(p1, p2):
    d = 0
    for i1, i2 in zip(p1, p2):
        d += abs(i2 - i1)
    return d

def in_const(c, p):
    for pc in c:
        if man_dist(pc, p) <= 3:
            return True
    return False

parsed = map(parse, sys.stdin)

cs = []

for p in parsed:
    added_to = None
    for c in cs:
        if in_const(c, p):
            if added_to:
                cs.remove(c)
                added_to.extend(c)
            else:
                c.append(p)
                added_to = c
    if not added_to:
        cs.append([p])

print(len(cs))
