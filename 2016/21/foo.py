import sys

def parse(line):
    return line.split()

def scramble(s):
    s = list(s)
    for i in ins:
        o = i[0]

        if o == "swap":
            if i[1] == "position":
                x, y = int(i[2]), int(i[-1])
                a = s[x]
                s[x] = s[y]
                s[y] = a
            else:
                x, y = i[2], i[-1]
                ix = s.index(x)
                iy = s.index(y)
                a = s[ix]
                s[ix] = s[iy]
                s[iy] = a
        elif o == "rotate":
            d = i[1]

            if d == "left":
                r = len(s) - int(i[2])
            elif d == "right":
                r = int(i[2])
            else:
                ix = s.index(i[-1])
                r = 1 + ix
                if ix >= 4:
                    r += 1
            r %= len(s)
            s = s[-r:] + s[:-r]
        elif o == "reverse":
            x, y = int(i[2]), int(i[4])
            s = s[:x] + list(reversed(s[x:y+1])) + s[y+1:]
        elif o == "move":
            x, y = int(i[2]), int(i[5])
            a = s.pop(x)
            s.insert(y, a)
    return s

def unscramble(s):
    s = list(s)
    for i in reversed(ins):
        o = i[0]

        if o == "swap":
            if i[1] == "position":
                x, y = int(i[2]), int(i[-1])
                a = s[x]
                s[x] = s[y]
                s[y] = a
            else:
                x, y = i[2], i[-1]
                ix = s.index(x)
                iy = s.index(y)
                a = s[ix]
                s[ix] = s[iy]
                s[iy] = a
        elif o == "rotate":
            d = i[1]

            if d == "left" or d == "right":
                if d == "left":
                    r = len(s) - int(i[2])
                elif d == "right":
                    r = int(i[2])
                r %= len(s)
                r = len(s) - r
                s = s[-r:] + s[:-r]
            else:
                ix = s.index(i[-1])
                # try moving back on number at a time
                for dd in range(1, len(s) + 2):
                    # find the new index with a move of this distance
                    ni = ix - dd
                    # normalize
                    ni %= len(s)
                    # now try to move back
                    rr = 1 + ni
                    if ni >= 4:
                        rr += 1
                    # if we didn't end up at the same position, skip
                    if (ni + rr) % len(s) != ix:
                        continue
                    # this distance worked, go with that
                    dd %= len(s)
                    dd = -dd
                    s = s[-dd:] + s[:-dd]
                    break
        elif o == "reverse":
            x, y = int(i[2]), int(i[4])
            s = s[:x] + list(reversed(s[x:y+1])) + s[y+1:]
        elif o == "move":
            x, y = int(i[2]), int(i[5])
            a = s.pop(y)
            s.insert(x, a)
    return s

ins = map(parse, sys.stdin)

part1 = list(sys.argv[1])
part2 = list(sys.argv[2])

print("".join(scramble(part1)))
print("".join(unscramble(part2)))
