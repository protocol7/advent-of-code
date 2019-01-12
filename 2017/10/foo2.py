import sys

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

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

def hash(inp):
    s = list(range(256))
    lens = [ord(c) for c in inp.strip()]
    lens = lens + [17, 31, 73, 47, 23]
    pos = 0
    skip = 0
    for round in range(64):
        for ll in lens:
            # reverse
            xx = s[:]
            s = rotate(s, pos, ll)

            # move
            pos = (pos + ll + skip) % len(s)

            skip += 1

    dense = [reduce(lambda x, y: x ^ y, block) for block in chunks(s, 16)]

    return "".join([format(d, '02x') for d in dense])

if len(sys.argv) > 1:
    inp = sys.argv[1]
else:
    inp = sys.stdin.read()

print(hash(inp))
