import sys
from collections import *
from util import *

def parse(line):
    return line.strip().split()

xs = list(map(parse, sys.stdin))

# one "function" for model number digit
p = defaultdict(list)

i = -1
for x in xs:
    if x[0] == "inp":
        i += 1

    p[i].append(x)

def run(inp, i, z):
    d = {
        "w": 0,
        "x": 0,
        "y": 0,
        "z": z,
    }

    xs = p[inp]

    # first instruction is always input
    d[xs[0][1]] = i

    for x in xs[1:]:
        op = x[0]
        a = x[1]
        b = x[2]
        b = int(b) if isint(b) else d[b]

        if op == "add":
            d[a] = d[a] + b
        elif op == "mul":
            d[a] = d[a] * b
        elif op == "div":
            d[a] = int(d[a] / b)
        elif op == "mod":
            d[a] = d[a] % b
        elif op == "eql":
            d[a] = int(d[a] == b)

    return d["z"]


good_z = {0: [""]}

for r in range(13, -1, -1):
    print("round", r)
    ngz = defaultdict(list)

    for i in range(1, 10):
        # 200000 found through trial and error
        for z in range(200000):
            oz = run(r, i, z)

            if oz in good_z:
                ngz[z] += [str(i) + gg for gg in good_z[oz]]

    good_z = ngz

print(min(good_z[0]), max(good_z[0]))
