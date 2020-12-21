import sys

def parse(line):
    return line.strip()

a, _, c = sys.stdin.read().split("\n\n")

ranges = []
for line in a.split("\n"):
    rs = line.split(": ")[1]
    for r in rs.split(" or "):
        rr = tuple(map(int, r.split("-")))
        ranges.append(rr)

c = c.split()[2:]

rate = 0
for line in c:
    for x in map(int, line.strip().split(",")):
        if not any(d <= x <= e for d, e in ranges):
            rate += x

print(rate)