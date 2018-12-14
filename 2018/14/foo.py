import sys

inp = int(sys.argv[1])

rec = [3, 7]
elfs = [0, 1]

def digits(i):
    return map(int, str(i))

for _ in range(inp + 10):
    s = sum([rec[e] for e in elfs])
    rec.extend(digits(s))

    # move
    def pos(elf, p):
        return (elf + p + 1) % len(rec)
    elfs = [pos(e, rec[e]) for e in elfs]

s = "".join([str(i) for i in rec])

print(s[inp:inp+10])
