import sys
from collections import *
from itertools import *

with open("challenge.bin", "rb") as f:
    data = f.read()

mem = [0] * pow(2, 15)
regs = [0] * 8
stack = []

for i in range(0, len(data), 2):
    a, b = data[i], data[i+1]
    x = (b << 8) + a

    mem[i//2] = x

ip = 0

def read(x):
    if 0 <= x <= 32767:
        return x
    elif 32768 <= x <= 32775:
        r = x - 32768
        if r == 7:
            if ip > 600: # skip self test
                # patch memory
                mem[5485] = 6 # set value of r0 to the expected output of the recursive function
                mem[5489] = 21 # nop to skip call to recursive function
                mem[5490] = 21 # as above

                return 25734 # found from fun.rs
        return regs[r]

def reg(x):
    return x - 32768

# walk around the cake and pick up items
inp = """
take tablet
doorway
north
north
bridge
continue
down
east
take empty lantern
west
west
passage
ladder
west
south
north
take can
west
use tablet
use can
use lantern
ladder
darkness
continue
west
west
west
west
north
take red coin
north
north
"""

# in equation room, found equation:
# _ + _ * _^2 + _^3 - _ = 399

# pick up coins
inp += """
east
take concave coin
down
take corroded coin
up
west
west
take blue coin
up
take shiny coin
down
east
"""

# back in equation room, use coins
# solved equation in coins.py
inp += """
use blue coin
use red coin
use shiny coin
use concave coin
use corroded coin
"""

# use teleporter, this will trigger the patching of registry/memory above
inp += """
north
take teleporter
use teleporter
"""

# office, this is where we end up without registry/memory patching
#inp += "take business card\n"
#inp += "look business card\n"
#inp += "take strange book\n"
#inp += "look strange book\n"

# beach, this is where we end up with registry/memory patching
inp += """
north
north
north
north
north
north
north
east
take journal
look journal
west
north
north
"""

# equation, solved in vault.py
# 22 + 4 - 11 * 4 - 18 - 11 - 1

inp += """
take orb
north
east
east
north
west
south
east
east
west
north
north
east
vault
take mirror
use mirror
"""

# UwdiYuvVYIIV
# VIIYVvUYibwU # mirrored

ff = open("trace.txt", "w")

def trace(ip, op, reg, *args):
    s = str(ip) + ": " + op + " "
    if reg:
        s += "$%s, " % reg

    s += ", ".join(map(str, args))
    ff.write(s + "\n")

def disassemble():
    with open("disassembly.txt", "w") as f:

        def p(ip, op, reg, *args):
            s = "%s: %s " % (ip, op)
            if reg:
                r = reg - 32768
                s += "r%s, " % r

            def rr(x):
                if x >= 32768:
                    return "r%s" % (x - 32768)
                else:
                    return str(x)

            s += ", ".join(map(rr, args))
            f.write(s + "\n")

        ip = 0
        while ip + 1 < len(mem):
            op = mem[ip]

            if op == 0:
                p(ip, "halt", None)
                ip += 1
            elif op == 1:
                p(ip, "set", mem[ip+1], mem[ip+2])
                ip += 3
            elif op == 2:
                p(ip, "push", None, mem[ip+1])
                ip += 2
            elif op == 3:
                p(ip, "pop", mem[ip+1])
                ip += 2
            elif op == 4 or op == 5:
                oo = "eq" if op == 4 else "gt"
                p(ip, oo, mem[ip+1], mem[ip+2], mem[ip+3])
                ip += 4
            elif op == 6:
                p(ip, "jmp", None, mem[ip+1])
                ip += 2
            elif op == 7:
                p(ip, "jt", None, mem[ip+1], mem[ip+2])
                ip += 3
            elif op == 8:
                p(ip, "jf", None, mem[ip+1], mem[ip+2])
                ip += 3
            elif op == 9 or op == 10 or op == 11:
                if op == 9:
                    oo = "add"
                elif op == 10:
                    oo = "mul"
                elif op == 11:
                    oo = "mod"

                p(ip, oo, mem[ip+1], mem[ip+2], mem[ip+3])
                ip += 4
            elif op == 12 or op == 13:
                if op == 12:
                    oo = "and"
                elif op == 13:
                    oo = "or"

                p(ip, oo, mem[ip+1], mem[ip+2], mem[ip+3])
                ip += 4
            elif op == 14:
                p(ip, "not", mem[ip+1], mem[ip+2])
                ip += 3
            elif op == 15:
                p(ip, "rmem", mem[ip+1], mem[ip+2])
                ip += 3
            elif op == 16:
                p(ip, "wmem", None, mem[ip+1], mem[ip+2])
                ip += 3
            elif op == 17:
                p(ip, "call", None, mem[ip+1])
                ip += 2
            elif op == 18:
                p(ip, "ret", None)
                ip += 1
            elif op == 19:
                p(ip, "out", None, mem[ip+1])
                ip += 2
            elif op == 20:
                p(ip, "in", mem[ip+1])
                ip += 2
            elif op == 21:
                ip += 1
            else:
                # some unknown data, skip
                ip += 1


while True:
    op = mem[ip]

    if op == 0:  # halt
        break
    elif op == 1:  # set: 1 a b, set register <a> to the value of <b>
        a = reg(mem[ip + 1])
        b = read(mem[ip + 2])

        trace(ip, "set", a, b)

        regs[a] = b
        ip += 3
    elif op == 2: # push: 2 a, push <a> onto the stack
        a = read(mem[ip + 1])

        trace(ip, "push", None, a)

        stack.append(a)

        ip += 2
    elif op == 3: # pop: 3 a, remove the top element from the stack and write it into <a>; empty stack = error
        a = reg(mem[ip + 1])

        trace(ip, "pop", a)

        x = stack.pop()
        regs[a] = x

        ip += 2
    elif op == 4 or op == 5:
        # eq: 4 a b c, set <a> to 1 if <b> is equal to <c>; set it to 0 otherwise
        # gt: 5 a b c, set <a> to 1 if <b> is greater than <c>; set it to 0 otherwise

        a = reg(mem[ip + 1])
        b = read(mem[ip + 2])
        c = read(mem[ip + 3])

        if op == 4:
            oo = "eq"
        else:
            oo = "gt"

        trace(ip, oo, a, b, c)

        if op == 4 and b == c:
            regs[a] = 1
        elif op == 5 and b > c:
            regs[a] = 1
        else:
            regs[a] = 0

        ip += 4
    elif op == 6: # jmp, jump to <a>
        a = read(mem[ip + 1])

        trace(ip, "jmp", None, a)

        ip = a
    elif op == 7 or op == 8:
        # jt, if <a> is nonzero, jump to <b>
        # jf: 8 a b, if <a> is zero, jump to <b>

        a = read(mem[ip + 1])
        b = read(mem[ip + 2])

        oo = "jt" if op == 7 else "jf"

        trace(ip, oo, None, a, b)

        if op == 7 and a != 0:
            ip = b
        elif op == 8 and a == 0:
            ip = b
        else:
            ip += 3
    elif op == 9 or op == 10 or op == 11:
        # add: 9 a b c, assign into <a> the sum of <b> and <c> (modulo 32768)
        # mult: 10 a b c, store into <a> the product of <b> and <c> (modulo 32768)
        # mod: 11 a b c, store into <a> the remainder of <b> divided by <c>

        a = reg(mem[ip + 1])
        b = read(mem[ip + 2])
        c = read(mem[ip + 3])

        if op == 9:
            oo = "add"
            x = (b + c) % 32768
        elif op == 10:
            oo = "mul"
            x = (b * c) % 32768
        elif op == 11:
            oo = "mod"
            x = b % c

        trace(ip, oo, a, b, c)

        regs[a] = x
        ip += 4
    elif op == 12 or op == 13:
        # and: 12 a b c, stores into <a> the bitwise and of <b> and <c>
        # or: 13 a b c, stores into <a> the bitwise or of <b> and <c>

        a = reg(mem[ip + 1])
        b = read(mem[ip + 2])
        c = read(mem[ip + 3])

        if op == 12:
            oo = "and"
            x = b & c
        elif op == 13:
            oo = "or"
            x = b | c

        trace(ip, oo, a, b, c)

        regs[a] = x

        ip += 4
    elif op == 14: # not: 14 a b, stores 15-bit bitwise inverse of <b> in <a>
        a = reg(mem[ip + 1])
        b = read(mem[ip + 2])

        trace(ip, "not", a, b)

        x = ~b
        x = x & 0b111111111111111

        regs[a] = x

        ip += 3
    elif op == 15: # rmem: 15 a b, read memory at address <b> and write it to <a>
        a = reg(mem[ip + 1])
        b = mem[read(mem[ip + 2])]

        trace(ip, "rmem", a, b)

        regs[a] = b

        ip += 3
    elif op == 16: # wmem: 16 a b, write the value from <b> into memory at address <a>
        a = read(mem[ip + 1])
        b = read(mem[ip + 2])

        trace(ip, "wmem", None, a, b)

        mem[a] = b

        ip += 3
    elif op == 17: # call: 17 a, write the address of the next instruction to the stack and jump to <a>
        a = read(mem[ip + 1])

        trace(ip, "call", None, a)

        stack.append(ip+2)

        ip = a
    elif op == 18: # ret: 18, remove the top element from the stack and jump to it; empty stack = halt
        trace(ip, "ret", None)

        ip = stack.pop()
    elif op == 19:
        a = read(mem[ip + 1])
        print(chr(a), end='')
        ip += 2
    elif op == 20: # in: 20 a, read a character from the terminal and write its ascii code to <a>; it can be assumed that once input starts, it will continue until a newline is encountered; this means that you can safely read whole lines from the keyboard and trust that they will be fully read
        a = reg(mem[ip + 1])

        # we're out of prepared input, switch to manual input mode
        if not inp:
            inp = input()
            inp += "\n"

        regs[a] = ord(inp[0])
        inp = inp[1:]

        ip += 2
    elif op == 21:  # noop
        ip += 1
    else:
        assert False, "Unknown opcode: %s" % op