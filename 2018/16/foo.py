import sys
import re

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

ops = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri,
        gtrr, eqir, eqri, eqrr]

def parse(lines):
    states = list()
    for i in range(0, len(lines), 4):
        before = [int(x) for x in re.findall("\d+", lines[i])]
        op = [int(x) for x in re.findall("\d+", lines[i+1])]
        after = [int(x) for x in re.findall("\d+", lines[i+2])]
        states.append((op, before, after))
    return states

samples_input, _ = sys.stdin.read().split("\n\n\n")

samples = parse(samples_input.split("\n"))

m = 0
for (op, a, b, c), before, after in samples:
    matching = 0
    for o in ops:
        r = before[:]
        o(a, b, c, r)
        if r == after:
            matching += 1
    if matching > 2:
        m += 1

print(m)
