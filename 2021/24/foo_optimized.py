import sys
from collections import *
from util import *

def parse(line):
    return line.strip().split()

xs = list(map(parse, sys.stdin))

# one "function" per model number digit
p = defaultdict(list)

i = -1
for x in xs:
    if x[0] == "inp":
        i += 1

    p[i].append(x)

# only three instructions varies based on parameters
params = {}
for i, x in p.items():
    params[i] = [int(x[a][2]) for a in (4, 5, 15)]

def fun(w, z, a, b ,c):
    # mul x 0
    # add x z
    # mod x 26
    # add x 12
    x = z % 26 + b

    # div z 1
    z = int(z / a)
  
    # eql x w
    # eql x 0
    if x == w:
        return z
    else:
        # mul y 0
        # add y 25
        # mul y x
        # add y 1
        z *= 26
    
        # mul y 0
        # add y w
        # add y 1
        # mul y x
        # add z y
        z += w + c

    return z


good_z = {0: [0]}

for r in range(13, -1, -1):
    a, b, c = params[r]

    ngz = defaultdict(list)
    for i in range(1, 10):
        # 200000 found through trial and error
        for z in range(200000):
            oz = fun(i, z, a, b, c)

            if oz in good_z:
                # add digit on the left
                l = 10**(13 - r) * i
                
                ngz[z] += [l + gg for gg in good_z[oz]]

    good_z = ngz

print(min(good_z[0]), max(good_z[0]))