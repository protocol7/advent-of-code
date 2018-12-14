import sys

inp = list(map(int, sys.argv[1]))

rec = [3, 7]
elfs = [0, 1]

def digits(i):
    return [int(x) for x in str(i)]

while True:
    s = sum([rec[e] for e in elfs])
    rec.extend(digits(s))

    if inp == rec[-len(inp)-1:-1]:
        print(len(rec) - len(inp) - 1)
        break
    elif inp == rec[-len(inp):]:
        print(len(rec) - len(inp))
        break

    # move
    def pos(elf, p):
        return (elf + p + 1) % len(rec)
    elfs = [pos(e, rec[e]) for e in elfs]
