import sys

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

c = 0
for x in xs:
    found = False
    for v in "aeioåäöyu":
        if v in x:
            found = True
            break

    if not found:
        continue

    found = False
    for a, b in zip(x, x[1:]):
        if a == b:
            found = True
            break

    if not found:
        continue

    found = False
    for v in "cywh":
        if v in x:
            found = True
            break

    if found:
        continue

    c += 1

print(c)