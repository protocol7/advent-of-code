import sys
from itertools import count

def parse(line):
    return line.split()

ins = map(parse, sys.stdin)

def v(x, reg):
    if x in reg:
        return reg[x]
    else:
        return int(x)

def run(a, ml):
    reg = {
            "a": a,
            "b": 0,
            "c": 0,
            "d": 0
            }
    out = []
    i = 0
    while i >= 0 and i < len(ins) and len(out) < ml:
        if i == 3 and False:
            print("hack!")
            reg["d"] = reg["c"] * reg["b"] - 1
            reg["c"] = 1
            reg["b"] = 1

        ii = ins[i]
        o = ii[0]
        if o == "cpy":
            x = v(ii[1], reg)
            y = ii[2]
            reg[y] = x
        elif o == "inc":
            reg[ii[1]] += 1
        elif o == "dec":
            reg[ii[1]] -= 1
        elif o == "jnz":
            x = v(ii[1], reg)
            y = v(ii[2], reg)
            if x != 0:
                i += y - 1
        elif o == "out":
            x = v(ii[1], reg)
            out.append(x)

        i += 1
    return out

ml = 10 # reasonable match length, if it's a 0, 1 series for ml outputs, we're happy
for i in count():
    out = run(i, ml)
    if out == [0, 1] * (ml // 2):
        print(i)
        break
