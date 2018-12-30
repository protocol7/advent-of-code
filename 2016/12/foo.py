import sys

def parse(line):
    return line.split()

ins = map(parse, sys.stdin)

reg = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0
        }

def v(x):
    if x in reg:
        return reg[x]
    else:
        return int(x)

reg["c"] = 1
i = 0
while i >= 0 and i < len(ins):
    ii = ins[i]
    o = ii[0]
    if o == "cpy":
        x = v(ii[1])
        y = ii[2]
        reg[y] = x
    elif o == "inc":
        reg[ii[1]] += 1
    elif o == "dec":
        reg[ii[1]] -= 1
    elif o == "jnz":
        x = v(ii[1])
        y = ii[2]
        if x != 0:
            i += int(y) - 1
    i += 1

print(reg["a"])
