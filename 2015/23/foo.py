import sys

def parse(line):
    return [s.strip(",") for s in line.strip().split()]

instr = map(parse, sys.stdin)
i = 0

reg = {
        "a": int(sys.argv[1]),
        "b": 0
        }

while i >= 0 and i < len(instr):
    ins = instr[i]
    o = ins[0]
    r = ins[1]
    if o ==  "hlf":
        reg[r] //= 2
    elif o ==  "tpl":
        reg[r] *= 3
    elif o ==  "inc":
        reg[r] += 1
    elif o ==  "jmp":
        i += (int(r) - 1)
    elif o ==  "jie":
        if reg[r] % 2 == 0:
            i += (int(ins[2]) - 1)
    elif o ==  "jio":
        if reg[r] == 1:
            i += (int(ins[2]) - 1)
    else:
        assert False

    i += 1

print(reg["b"])
