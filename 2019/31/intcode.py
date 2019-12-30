import sys
from collections import defaultdict

def parse(f):
    return map(int, f.read().strip().split(","))[:]

def opcode(i):
    if i == 1:
        return "add"
    elif i == 2:
        return "mul"
    elif i == 3:
        return "input"
    elif i == 4:
        return "output"
    elif i == 5:
        return "jump-if-true"
    elif i == 6:
        return "jump-if-false"
    elif i == 7:
        return "less-than"
    elif i == 8:
        return "equal"
    elif i == 9:
        return "base"
    else:
        assert False

def digit(number, n):
    return number // 10**n % 10

class Intcode:
    def __init__(self, prog, inp):
        self.prog = defaultdict(int)
        for i, p in enumerate(prog):
            self.prog[i] = p

        self.i = 0
        self.input = inp
        self.base = 0

    def run(self, debug=False):
        while True:
            start_prog = dict(self.prog)
            start_i = self.i
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
                    elif modes[u] == 2:
                        x = self.base + pp
                        res.append(self.prog[x])
                    else:
                        assert False

                for u in range(out):
                    pp = self.prog[self.i+u+1+inn]
                    if modes[u+inn] == 0:
                        res.append(pp)
                    elif modes[u+inn] == 2:
                        res.append(self.base + pp)
                    else:
                        assert False

                used_params.extend(res)
                return res if len(res) > 1 else res[0]

            if o == 1: # add
                a, b, c = params(2, 1)
                self.prog[c] = a + b
                self.i += 4
            elif o == 2: # mult
                a, b, c = params(2, 1)
                self.prog[c] = a * b
                self.i += 4
            elif o == 3: #input
                x = self.input()
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
            elif o == 9: # base
                a = params(1, 0)
                self.base += a
                #print(a, self.base)
                self.i += 2
            elif o == 99: # exit
                return None
            else:
                assert False, "unknown op %s" % o

            if debug:
                self.halt(start_prog, start_i, op, o, modes, used_params)

    def halt(self, start_prog, start_i, op, o, modes, used_params):
        print("op: %s, i: %s -> %s, modes: %s, params: %s, base: %s" % (opcode(o), start_i, self.i, modes, used_params, self.base))

        major = 30
        minor = 10
        s = ""
        row = 0
        for x in range(1024):
            p1 = start_prog.get(x, 0)
            p2 = self.prog.get(x, 0)
            if s and x % major == 0:
                print("%-5s: %s" % (row, s))
                row += major
                s = ""
            elif s and x % minor == 0:
                s += ", "
            if p1 == p2:
                if x >= start_i and x <= start_i + len(used_params):
                    s += "\033[92m%-6s\033[0m" % p2
                else:
                    s += "%-6s" % p2
            else:
                s += "\033[91m%s -> %s\033[0m " % (p1, p2)
        if s:
            print("%-5s: %s" % (row, s))

        raw_input("")
