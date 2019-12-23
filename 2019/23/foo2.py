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
    nat = None
    last_nat = None

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
                        nat = (x, y)
                    else:
                        _, oq = nics[o]
                        oq.append((x, y))

                    o = ic.run(-1)

        # are all queues empty?
        empty = all([not q for _, q in nics.values()])

        if empty:
            _, q = nics[0]
            q.append(nat)
            print("nat", y)
            if last_nat == nat:
                _, y = nat
                return y
            last_nat = nat

print(run())
