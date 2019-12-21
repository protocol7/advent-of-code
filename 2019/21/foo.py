import sys
from intcode import *

inp = []
inp_iter = iter(inp)
prog = parse(open("input.txt"))
ic = Intcode(prog, lambda: next(inp_iter))

instructions = 0
for line in sys.stdin:
    t = line.split("#")[0]
    t = t.strip()
    if t:
        instructions += 1
        print(t)
        for c in t:
            inp.append(ord(c))
        inp.append(10)

print("%s instructions" % instructions)
assert instructions < 16

s = ""
pos = 0
while True:
    o = ic.run()

    if o is None:
        print("done")
        break
    if o > 256:
        print(o)
    elif o == 10:
        if "@" in s:
            pos = s.index("@")

        print(s)

        if "#" in s:
            print((" " * (pos + 1)) + "ABCDEFGHI")

        s = ""
    else:
        s += chr(o)
