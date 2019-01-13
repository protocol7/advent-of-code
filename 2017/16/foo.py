import sys

def parse(line):
    return line.strip().split(",")

instrs = parse(sys.stdin.read())
size = int(sys.argv[1])

progs = [chr(i + ord("a")) for i in range(size)]

for s in instrs:
    o = s[0]

    if o == "s":
        x = int(s[1:])
        progs = progs[-x:] + progs[:-x]
    elif o == "x":
        a, b = [int(i) for i in s[1:].split("/")]
        x = progs[a]
        progs[a] = progs[b]
        progs[b] = x
    elif o == "p":
        a, b = s[1:].split("/")
        ia = progs.index(a)
        ib = progs.index(b)
        x = progs[ia]
        progs[ia] = progs[ib]
        progs[ib] = x
    else:
        assert False

print("".join(progs))
