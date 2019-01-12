import sys

def parse(line):
    return [int(i) for i in line.split(":")]

parsed = map(parse, sys.stdin)

fw = {d:(0, r, 1) for d, r in parsed}

last = max(fw.keys())

severity = 0
for p in range(last + 1):
    # move packet
    if p in fw:
        s, r, _ = fw[p]
        if s == 0:
            severity += p * r

    # move scanners
    for d, (pos, r, dir) in fw.iteritems():
        pos = pos + dir
        if pos == 0 or pos == r - 1:
            dir = -dir

        fw[d] = (pos, r, dir)

print(severity)
