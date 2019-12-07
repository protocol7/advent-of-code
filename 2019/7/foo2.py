import sys
from itertools import *
from util import *

def parse(f):
    return map(int, f.read().strip().split(","))[:]

class Intcode:
    def __init__(self, prog, inp=[]):
        self.prog = prog[:]
        self.i = 0
        self.input = inp[:]
        self.input_iter = iter(self.input)

    def run(self, debug=False):
        while True:
            op = self.prog[self.i]

            o = op % 100
            modes = [digit(op, x) for x in range(2, 5)]

            used_params = []
            def params(inn, out=0):
                res = []
                for u in range(inn):
                    pp = self.prog[self.i+u+1]
                    if modes[u] == 0:
                        res.append(self.prog[pp])
                    elif modes[u] == 1:
                        res.append(pp)
                    else:
                        assert False

                for u in range(out):
                    pp = self.prog[self.i+u+1+inn]
                    res.append(pp)
                used_params.extend(res)
                if len(res) > 1:
                    return res
                elif len(res) == 1:
                    return res[0]
                else:
                    assert False

            if o == 1: # add
                a, b, c = params(2, 1)
                self.prog[c] = a + b
                self.i += 4
            elif o == 2: # mult
                a, b, c = params(2, 1)
                self.prog[c] = a * b
                self.i += 4
            elif o == 3: #input
                x = next(self.input_iter)
                a = params(0, 1)
                self.prog[a] = x
                self.i += 2
            elif o == 4: # output
                a = params(1)
                self.i += 2
                return a
            elif o == 5: # jump if true
                a, b = params(2)
                if a != 0:
                    self.i = b
                else:
                    self.i += 3
            elif o == 6: # jump if false
                a, b = params(2)
                if a == 0:
                    self.i = b
                else:
                    self.i += 3
            elif o == 7: # less than
                a, b, c = params(2, 1)
                self.prog[c] = int(a<b)
                self.i += 4
            elif o == 8: # equals
                a, b, c = params(2, 1)
                self.prog[c] = int(a==b)
                self.i += 4
            elif o == 99: # exit
                return None
            else:
                assert False, "unknown op %s" % o

prog = parse(sys.stdin)

def rr(phases):
    amps = [Intcode(prog, [p]) for p in phases]

    o = 0
    while True:
        for a in amps:
            a.input.append(o)
            x = a.run()
            if x is None:
                return o
            else:
                o = x

print(max([rr(p) for p in permutations(range(5, 10))]))
