import sys
from util import *

def parse(line):
    return intify(line.split())

p = list(map(parse, sys.stdin))

def run(p):
    acc = 0
    ip = 0
    seen = set()

    while True:
        if ip >= len(p):
            print(acc)
            return True

        if ip in seen:
            return False
        seen.add(ip)

        a, b = p[ip]

        if a == "acc":
            acc += b
            ip += 1
        elif a == "jmp":
            ip += b
        elif a == "nop":
            ip += 1

for i, (a, b) in enumerate(p):
    pp = p[:]

    if a == "jmp":
        pp[i] = ("nop", b)
    elif a == "nop":
        pp[i] = ("jmp", b)
    else:
        continue

    if run(pp):
        break
