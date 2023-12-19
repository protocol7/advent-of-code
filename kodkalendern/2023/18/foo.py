import sys

def parse(line):
    return line.strip()

consonants = set("bcdfghjklmnpqrstvwxz")

xs = list(map(parse, sys.stdin))

def norm(x):
    return tuple(c in consonants for c in x)

def flip(x):
    return tuple(not c for c in x)

norms = {norm(x): x for x in xs}

for norm, sid in norms.items():
    if flip(norm) not in norms:
        print(sid)
