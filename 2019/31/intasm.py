from collections import *
from util import *

def intasm(asm):
    lens = {
        "add": 4,
        "mul": 4,
        "inp": 2,
        "out": 2,
        "jit": 3,
        "jif": 3,
        "lt": 4,
        "eq": 4,
        "ext": 1,
        "rb": 2,
            }

    ll = 0
    labels = dict()
    vars = OrderedDict()
    for i in asm.split("\n"):
        i = i.split("#")[0].strip()
        if i:
            if ":" in i:
                label, i = [x.strip() for x in i.split(":")]
                labels[label] = ll
            i = i.split(" ")
            o = i[0]
            if o == "var":
                vars[i[1]] = i[2]
            elif o == "block":
                ll += int(i[1])
            else:
                ll += lens[o]

    ll = [ll] # hack!
    def next_mem():
        x = ll[0]
        ll[0] = x + 1
        return x

    regs = defaultdict(next_mem)

    # make sure vars are stored first
    for v in vars.keys():
        _ = regs[v]

    prog = []
    for i in asm.split("\n"):
        i = i.split("#")[0].strip()
        if i:
            if ":" in i:
                label, i = [x.strip() for x in i.split(":")]

            i = i.split(" ")
            o = i[0]
            i = i[1:]
            out = []
            if o == "add" or o == "mul":
                if o == "add":
                    op = "01"
                else:
                    op = "02"
                for x in i:
                    if isint(x):
                        op = "1" + op
                        out.append(int(x))
                    elif x[0] == "&":
                        op = "2" + op
                        out.append(int(x[1:]))
                    else:
                        op = "0" + op
                        out.append(regs[x])
            elif o == "inp":
                op = "03"
                out.append(regs[i[0]])
            elif o == "out":
                op = "04"
                x = i[0]
                if isint(x):
                    op = "1" + op
                    out.append(int(x))
                elif x[0] == "&":
                    op = "2" + op
                    out.append(int(x[1:]))
                else:
                    op = "0" + op
                    out.append(regs[x])
            elif o == "jit" or o == "jif":
                if o == "jit":
                    op = "05"
                else:
                    op = "06"

                x = i[0]
                if isint(x):
                    op = "1" + op
                    out.append(int(x))
                else:
                    op = "0" + op
                    out.append(regs[x])

                op = "1" + op
                out.append(labels[i[1]])
            elif o == "lt" or o == "eq":
                if o == "lt":
                    op = "07"
                else:
                    op = "08"
                for x in i:
                    if isint(x):
                        op = "1" + op
                        out.append(int(x))
                    else:
                        op = "0" + op
                        out.append(regs[x])
            elif o == "rb":
                op = "09"
                x = i[0]
                if isint(x):
                    op = "1" + op
                    out.append(int(x))
                else:
                    op = "0" + op
                    out.append(regs[x])
            elif o == "ext":
                op = "99"
            elif o == "var":
                continue
            elif o == "block":
                prog += [0] * int(i[0])
                continue
            else:
                print(o)
                assert False
            prog += ([int(op)] + out)

    for value in vars.values():
        if isint(value):
            prog.append(int(value))
        else:
            prog.append(regs[value])

    return prog
