import sys
from util import *

def parse(line):
    return line.strip()

xs = sys.stdin.read().strip()

bi = "".join(binary(int(x, 16), 4) for x in xs)

def r(s, n):
    out = ""
    for _ in range(n):
        out += next(s)

    return out

def read_packet(ss):
    r(ss, 3) # version
    ty = int(r(ss, 3), 2)

    if ty == 4:
        # literal

        lit = ""
        while True:
            ll = r(ss, 5)

            lit += ll[1:]
            
            if ll[0] == "0":
                break

        return int(lit, 2)
    else:
        # operator
        lt = r(ss, 1)

        if lt == "0":
            le = int(r(ss, 15), 2)

            ps = iter(r(ss, le))

            vs = read_packets(ps)
        else:
            le = int(r(ss, 11), 2)

            vs = []
            for _ in range(le):
                vs.append(read_packet(ss))

        if ty == 0:
            return sum(vs)
        elif ty == 1:
            return prod(vs)
        elif ty == 2:
            return min(vs)
        elif ty == 3:
            return max(vs)
        elif ty == 5:
            return int(vs[0] > vs[1])
        elif ty == 6:
            return int(vs[0] < vs[1])
        elif ty == 7:
            return int(vs[0] == vs[1])
            
def read_packets(ss):
    vv = []
    while ss:
        try:
            vv.append(read_packet(ss))
        except StopIteration:
            break

    return vv

print(read_packets(iter(bi))[0])
