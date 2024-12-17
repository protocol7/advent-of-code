#!/usr/bin/env python3

import sys
from util import ints

def parse(line):
    return line.strip()

lines = sys.stdin.read().strip().split('\n')

a = ints(lines[0])[0]
b = ints(lines[1])[0]
c = ints(lines[2])[0]
program = ints(lines[4])

ip = 0

out = []
while ip < len(program):
    opcode = program[ip]
    operand = program[ip+1]

    assert operand != 7

    if operand == 4:
        reg = a
    elif operand == 5:
        reg = b
    elif operand == 6:
        reg = c
    else:
        reg = operand

    if opcode == 0:
        # The adv instruction (opcode 0) performs division. The numerator is the value in the A register.
        # The denominator is found by raising 2 to the power of the instruction's combo operand.
        # (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.)
        # The result of the division operation is truncated to an integer and then written to the A register.
        a = a // (2 ** reg)
    elif opcode == 1:
        # The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal operand, then stores the result in register B.
        b = b ^ operand

    elif opcode == 2:
        # The bst instruction (opcode 2) calculates the value of its combo operand modulo 8
        # (thereby keeping only its lowest 3 bits), then writes that value to the B register.
        b = reg % 8

    elif opcode == 3:
        # The jnz instruction (opcode 3) does nothing if the A register is 0. However,
        # if the A register is not zero, it jumps by setting the instruction pointer to the value of
        # its literal operand; if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.
        if a != 0:
            ip = operand
            continue

    elif opcode == 4:
        # The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result in register B.
        # (For legacy reasons, this instruction reads an operand but ignores it.)

        b = b ^ c

    elif opcode == 5:
        # The out instruction (opcode 5) calculates the value of its combo operand modulo 8,
        # then outputs that value. (If a program outputs multiple values, they are separated by commas.)
        out.append(reg % 8)

    elif opcode == 6:
        # The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B register. (The numerator is still read from the A register.)
        b = a // (2 ** reg)

    elif opcode == 7:
        # The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the C register. (The numerator is still read from the A register.)

        c = a // (2 ** reg)

    ip += 2

print(",".join(map(str, out)))
