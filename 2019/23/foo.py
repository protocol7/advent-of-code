import sys
from intcode import *

prog = parse(sys.stdin)

nics = {}

for i in range(50):
    q = []
    ic = Intcode(prog)
    ic.run(i)
    nics[i] = (ic, q)

def run():
    while True:
        for i in range(50):
            ic, q = nics[i]

            # check if the computer wants to output packets
            o = ic.run(-1)
            while o is not None:
                x = ic.run(None)
                y = ic.run(None)
                _, oq = nics[o]
                oq.append((x, y))
                o = ic.run(-1)

            # drain queue
            while q:
                x, y = q.pop(0)
                o = ic.run(x)
                o = ic.run(y)

                while o is not None:
                    # outputting packet
                    x = ic.run(None)
                    y = ic.run(None)
                    if o == 255:
                        return y

                    _, oq = nics[o]
                    oq.append((x, y))

                    o = ic.run(-1)

print(run())
