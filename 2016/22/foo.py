import sys

def p(size):
    return int(size.strip("T"))

def parse(line):
    l = line.split()
    return l[0], p(l[2]), p(l[3])

def viable(disks):
    v = 0
    for a in disks:
        for b in disks:
            if a == b:
                continue
            if a[1] == 0:
                continue
            if a[1] <= b[2]:
                v += 1
    return v


disks = map(parse, list(sys.stdin)[2:])
print(viable(disks))
