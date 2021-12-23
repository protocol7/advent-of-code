import sys
from util import *

def parse(line):
    return line.strip()

xs = sys.stdin.read().strip()

bi = "".join(binary(int(x, 16), 4) for x in xs)

def r(s, n):
    return "".join(next(s) for _ in range(n))

def read_packet(ss):    
    ver = int(r(ss, 3), 2)
    ty = r(ss, 3)

    if ty == "100":
        # literal

        while r(ss, 5)[0] == "1":
            pass

        return ver
    else:
        # operator

        lt = r(ss, 1)

        if lt == "0":
            le = int(r(ss, 15), 2)

            ps = iter(r(ss, le))

            return read_packets(ps) + ver
        else:
            le = int(r(ss, 11), 2)

            return sum(read_packet(ss) for _ in range(le)) + ver

def read_packets(ss):
    v = 0
    while ss:
        try:
            v += read_packet(ss)
        except:
            break

    return v


vf = read_packets(iter(bi))

print(vf)
