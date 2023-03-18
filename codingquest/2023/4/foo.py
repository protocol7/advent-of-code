import sys
from util import *

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

d = {}
for x in xs:
    header, sender, seq, cs, msg = x[:4], x[4:12], int(x[12:14], 16), int(x[14:16], 16), x[16:]

    msg = [int(msg[i:i+2], 16) for i in range(0, len(msg), 2)]

    if sum(msg) % 256 == cs:
        d[seq] = join(chr(i) for i in msg)

print(join(d[k] for k in sorted(d.keys())))
