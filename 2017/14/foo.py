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

def b(h):
    out = ""
    for c in h:
        out += "{0:b}".format(int(c, 16)).zfill(4)
    return out

inp = sys.argv[1].strip()

used = 0
rows = []
for r in range(128):
    h = hash(inp + "-" + str(r))
    row = b(h)
    rows.append(row)
    used += b(h).count("1")


# part 1
print(used)

# part 2
c2r = {}
next_reg = 0
for y, row in enumerate(rows):
    for x, c in enumerate(row):
        if c == "1":
            # default region to previous value, or None
            reg = c2r.get((x-1, y))
            above = c2r.get((x, y - 1))

            if above:
                if reg:
                    if reg != above:
                        # merge regions
                        for coord, r in c2r.iteritems():
                            if r == above:
                                c2r[coord] = reg
                else:
                    # inherit from above
                    reg = above
            else:
                if not reg:
                    next_reg += 1
                    reg = next_reg

            c2r[(x, y)] = reg

print(len(set(c2r.values())))
