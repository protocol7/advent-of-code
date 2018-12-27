import sys
from collections import defaultdict

def parse(line):
    return line.split(" => ")

rep, mol = sys.stdin.read().split("\n\n")
rep = rep.splitlines()
rep = map(parse, rep)

d = defaultdict(set)
for k, v in rep:
    d[k].add(v)
rep = d

mol = mol.strip()

combos = set()
for i in range(len(mol)):
    for r, rr in rep.iteritems():
        if mol[i:].startswith(r):
            for x in rr:
                combos.add(mol[:i] + x + mol[i+len(r):])

print(len(combos))
