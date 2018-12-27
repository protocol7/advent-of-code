import sys
from random import shuffle

def parse(line):
    return line.split(" => ")

rep, mol = sys.stdin.read().split("\n\n")
rep = rep.splitlines()
rep = map(parse, rep)

mol = mol.strip()

steps = 0

while mol != "e":
    for r, s in rep:
        if s in mol:
            mol = mol.replace(s, r, 1)
            steps += 1

print(steps)
