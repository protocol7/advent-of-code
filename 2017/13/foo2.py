import sys
from itertools import count

def parse(line):
    return [int(i) for i in line.split(":")]

def scan(fw):
    # move scanners
    for d, (pos, r, dir) in fw.iteritems():
        pos = pos + dir
        if pos == 0 or pos == r - 1:
            dir = -dir

        fw[d] = (pos, r, dir)

parsed = map(parse, sys.stdin)

fwbak = {d:(0, r, 1) for d, r in parsed}

last = max(fwbak.keys())

for delay in count():
    if delay > 0:
        scan(fwbak)
    fw = dict(fwbak)

    caught = False
    for p in range(last + 1):
        # move packet
        #print(fw, p)
        if p in fw:
            s, r, _ = fw[p]
            if s == 0:
                caught = True
                break

        scan(fw)

    if not caught:
        print(delay)
        break
