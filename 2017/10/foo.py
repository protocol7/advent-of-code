import sys

def parse(line):
    return [int(i) for i in line.split(",")]

lens = parse(sys.stdin.read())
l = list(range(int(sys.argv[1])))

pos = 0
skip = 0

def rotate(l, pos, ll):
    s = pos
    e = pos + ll
    if e > len(l):
        e %= len(l)

    if e < s:
        r = list(reversed(l[s:] + l[:e]))
        l = r[-e:] + l[e:s] + r[:len(l) - s]
    else:
        l = l[:s] + list(reversed(l[s:e])) + l[e:]
    return l

for ll in lens:
    # reverse
    xx = l[:]
    l = rotate(l, pos, ll)
    assert len(xx) == len(l)

    # move
    pos = (pos + ll + skip) % len(l)

    skip += 1

print(l[0] * l[1])
