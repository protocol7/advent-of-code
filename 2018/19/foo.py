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

reg = [0, 0, 0, 0, 0, 0]
ip = 0

while True:
    if ip <0 or ip >= len(instrs):
        break

    op, a, b, c = instrs[ip]

    reg[ipb] = ip

    ops[op](a, b, c, reg)

    ip = reg[ipb]
    ip += 1

print(reg[0])
