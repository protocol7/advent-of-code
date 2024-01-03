import sys

def parse(line):
    return list(map(int, line.strip().split(",")))

xs = list(map(parse, sys.stdin))

# start state
ns = list(range(10))

for x in xs:
    for nisse, swap in enumerate(x):
        ns[nisse], ns[swap] = ns[swap], ns[nisse]

print(ns[4])
