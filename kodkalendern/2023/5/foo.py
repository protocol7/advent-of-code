import sys

def parse(line):
    return list(map(int, line.strip().split(", ")))

xs = map(parse, sys.stdin)

ss = 0
for m, o, t, p in xs:
    # På 1 mark går 8 öre. På 1 öre går 3 örtugar, och på 1 örtug går 8 penningar

    s = (m * 8 * 3 * 8) + (o * 3 * 8) + (t * 8) + p
    ss += s >= 1000

print(ss)
