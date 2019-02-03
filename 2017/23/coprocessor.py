import sys

def parse(line):
    instr, reg, value = line.split()
    return (instr, reg, value)

def get_value(r):
    if r in reg:
        return reg[r]
    else:
        return int(r)

instructions = map(parse, sys.stdin)

reg = dict()
for c in "abcdefgh":
    reg[c] = 0
#reg["a"] = 1

pos = 0
mults = 0
while 0 <= pos < len(instructions):
    instr, r, value = instructions[pos]

    val = get_value(value)

    if instr == "set":
        reg[r] = val
        pos += 1
    elif instr == "sub":
        reg[r] -= val
        pos += 1
    elif instr == "mul":
        reg[r] *= val
        pos += 1
        mults += 1
    elif instr == "jnz":
        pred = get_value(r)
        if pred != 0:
            pos += val
        else:
            pos += 1
    else:
        assert False

print(mults)
