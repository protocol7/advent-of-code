import sys

def match(c1, c2):
    return c1 != c2 and c1.lower() == c2.lower()

def react(p):
    i = 1;
    while i < len(p):
        if match(p[i-1], p[i]):
            p = p[:(i-1)] + p[(i+1):]
            i = max(i - 1, 1)
        else:
            i += 1

    return p

poly = list(sys.stdin)[0].strip()

chars = set([x.lower() for x in poly])

lengths = []
for char in chars:
    r = react(filter(lambda c: c.lower() != char, poly))

    lengths.append(len(r))

print(min(lengths))
