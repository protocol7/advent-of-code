import sys
from collections import Counter

def parse(line):
    return line.strip()

lines = list(map(parse, sys.stdin))

msg = ""
msg2 = ""
for i in range(len(lines[0])):
    c = Counter()
    for l in lines:
        c[l[i]] += 1
    msg += c.most_common()[0][0]
    msg2 += c.most_common()[-1][0]

print(msg)
print(msg2)
