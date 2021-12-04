import sys
from util import *

ls = sys.stdin.read().split("\n\n")

ns = intify(ls[0].split(","))

bs = []
for x in ls[1:]:
    b = [intify(f.split()) for f in x.strip().split("\n")]

    bs.append(b)

def score(b):
    return sum(x for x in flatten(b) if x != -1)

def run():
    rem = [False] * len(bs)

    for n in ns:
        for bi, b in enumerate(bs):
            for br in b:
                for ic, bc in enumerate(br):
                    if bc == n:
                        br[ic] = -1

            # check rows and cols
            for r in b + transpose(b):
                if all(x == -1 for x in r):
                    rem[bi] = True

                    if all(rem):
                        return score(b) * n

print(run())