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

reg["a"] = 12
i = 0
while i >= 0 and i < len(ins):
    if i == 5:
        # accelerate 12!
        reg["a"] = reg["d"] * reg["c"] - 1
        reg["c"] = 1
        reg["d"] = 1

    ii = ins[i]
    #print(reg, ii, i)
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
        y = v(ii[2])
        if x != 0:
            i += y - 1
    elif o == "tgl":
        x = v(ii[1])
        if i + x <= 0 or i + x < len(ins):
            target = ins[i + x]
            if len(target) == 2:
                if target[0] == "inc":
                    target[0] = "dec"
                else:
                    target[0] = "inc"
            elif len(target) == 3:
                if target[0] == "jnz":
                    target[0] = "cpy"
                else:
                    target[0] = "jnz"
    i += 1

print(reg["a"])

# does 12! and then switches loop, now does 89 * 77 => 479008453
