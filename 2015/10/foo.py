import sys

inp = sys.argv[1]
rounds = int(sys.argv[2])

def t(s):
    out = ""
    prev = None
    count = 0
    for c in s:
        if c == prev:
            count += 1
        elif prev is None:
            count += 1
            prev = c
        else:
            out += str(count) + prev
            count = 1
            prev = c
    out += str(count) + prev
    return out

s = inp
for _ in range(rounds):
    s = t(s)

print(len(s))
