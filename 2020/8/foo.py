import sys
from util import *

def parse(line):
    return intify(line.split())

p = list(map(parse, sys.stdin))

acc = 0
ip = 0
seen = set()

while ip not in seen:
    seen.add(ip)

    a, b = p[ip]

    if a == "acc":
        acc += b
        ip += 1
    elif a == "jmp":
        ip += b
    elif a == "nop":
        ip += 1

print(acc)