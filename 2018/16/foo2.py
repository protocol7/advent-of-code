import sys
from collections import defaultdict
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

all_ops = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri,
        gtrr, eqir, eqri, eqrr]

def parse(lines):
    states = list()
    for i in range(0, len(lines), 4):
        before = [int(x) for x in re.findall("\d+", lines[i])]
        op = [int(x) for x in re.findall("\d+", lines[i+1])]
        after = [int(x) for x in re.findall("\d+", lines[i+2])]
        states.append((op, before, after))
    return states

def possible(samples):
    m = defaultdict(lambda: set(all_ops))
    for (op, a, b, c), reg, after in samples:
        matching = set()
        for o in all_ops:
            r = reg[:]
            o(a, b, c, r)
            if r == after:
                matching.add(o)
        m[op] = m[op].intersection(matching)
    return m

def uniq(pos):
    opscodes = {k:v.pop() for k, v in pos.iteritems() if len(v) == 1}
    q = [x for x in opscodes.values()]
    while q:
        item = q.pop()
        for k, p in pos.iteritems():
            if len(p) > 1:
                p.discard(item)
                if len(p) == 1:
                    px = p.pop()
                    q.append(px)
                    opscodes[k] = px

    return opscodes

def parse_op(line):
    return [int(x) for x in line.split()]

sample_input, program_input = sys.stdin.read().split("\n\n\n")
samples = parse(sample_input.split("\n"))

# find all possible ops per opcode
pos = possible(samples)

# derivce unique ops per opscode
opcodes = uniq(pos)

# parse program
program = map(parse_op, program_input.strip().split("\n"))

# run program
reg = [0, 0, 0, 0]
for o, a, b, c in program:
    op = opcodes[o]
    op(a, b, c, reg)

print(reg[0])

