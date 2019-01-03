import sys

inp = int(sys.argv[1])

elfs = [(x + 1, 1) for x in range(inp)]

def turn(elfs):
    for i, (e, c) in enumerate(elfs):
        if c == 0:
            continue
        s = i + 1
        if s == len(elfs):
            s = 0
        se, sc = elfs[s]
        nc = c + sc
        elfs[i] = (e, nc)
        elfs[s] = (se, 0)

    return [(e, c) for e, c in elfs if c > 0]

while len(elfs) > 1:
    elfs = turn(elfs)

print(elfs[0][0])
