import sys

def addr(a, b, c, reg):
    reg[c] = reg[a] + reg[b]

def addi(a, b, c, reg):
    reg[c] = reg[a] + b

def mulr(a, b, c, reg):
    reg[c] = reg[a] * reg[b]

def muli(a, b, c, reg):
    reg[c] = reg[a] * b

def banr(a, b, c, reg):
    reg[c] = reg[a] & reg[b]

def bani(a, b, c, reg):
    reg[c] = reg[a] & b

def borr(a, b, c, reg):
    reg[c] = reg[a] | reg[b]

def bori(a, b, c, reg):
    reg[c] = reg[a] | b

def setr(a, b, c, reg):
    reg[c] = reg[a]

def seti(a, b, c, reg):
    reg[c] = a

def gtir(a, b, c, reg):
    reg[c] = int(a > reg[b])

def gtri(a, b, c, reg):
    reg[c] = int(reg[a] > b)

def gtrr(a, b, c, reg):
    reg[c] = int(reg[a] > reg[b])

def eqir(a, b, c, reg):
    reg[c] = int(a == reg[b])

def eqri(a, b, c, reg):
    reg[c] = int(reg[a] == b)

def eqrr(a, b, c, reg):
    reg[c] = int(reg[a] == reg[b])

ops = {
        "addr": addr,
        "addi": addi,
        "mulr": mulr,
        "muli": muli,
        "banr": banr,
        "bani": bani,
        "borr": borr,
        "bori": bori,
        "setr": setr,
        "seti": seti,

        "gtir": gtir,
        "gtri": gtri,
        "gtrr": gtrr,

        "eqir": eqir,
        "eqri": eqri,
        "eqrr": eqrr
        }

def parse(line):
    op, a, b, c = line.strip().split()
    a = int(a)
    b = int(b)
    c = int(c)
    return op, a, b, c

inp = list(sys.stdin)

ipb = int(inp[0].split()[1])

instrs = map(parse, inp[1:])

reg = [1, 0, 0, 0, 0, 0]
ip = 0

counter = 0
while True:
    counter += 1
    if ip <0 or ip >= len(instrs):
        break

    op, a, b, c = instrs[ip]
    oo = ops[op]

    # allow for bootstrapping
    if counter > 20:
        product = reg[2]
        if op == "mulr":
            # speed things up a bit by jumping straight to the productber factors
            if reg[3] * reg[5] > product:
                # already larger than the product, no need to continue
                reg[5] = product
            elif reg[3] > 555337:
                # larger than the largest factor, skip to product itself
                reg[3] = product
                reg[5] = 1
            elif reg[3] > 19:
                # larger than the smaller fqctor, skip to the larger factor
                reg[3] = 555337
                reg[5] = 19
            elif reg[3] == 19:
                # at smaller factor, skip to other factor
                reg[5] = 555337
            elif reg[3] == 1:
                # at 1, skip to product
                reg[5] = product
            elif product % reg[3] > 0:
                # this will never work, skip
                reg[5] = product

    reg[ipb] = ip
    rr = reg[:]

    oo(a, b, c, reg)

    ip = reg[ipb]
    ip += 1

print(reg[0])
