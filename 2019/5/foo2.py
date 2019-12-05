import sys

def from_stdin():
    return map(int, list(sys.stdin)[0].strip().split(","))[:]

def run(prog, inp):
    p = prog[:]

    i = 0

    while True:
        op = p[i]

        o = op % 100
        modes = [0,0,0,0] # pad with some zeros

        s = str(op)
        for x in range(len(s) - 2):
            modes.insert(0, int(s[x]))

        def params(inn, out=0):
            res = []
            for u in range(inn):
                pp = p[i+u+1]
                if modes[u] == 0:
                    res.append(p[pp])
                elif modes[u] == 1:
                    res.append(pp)
                else:
                    assert False

            for u in range(out):
                pp = p[i+u+1+inn]
                res.append(pp)
            if len(res) > 1:
                return res
            elif len(res) == 1:
                return res[0]
            else:
                assert False

        if o == 1: # add
            a, b, c = params(2, 1)
            p[c] = a + b
            i += 4
        elif o == 2: # mult
            a, b, c = params(2, 1)
            p[c] = a * b
            i += 4
        elif o == 3: #input
            a = params(0, 1)
            p[a] = inp
            i += 2
        elif o == 4: # output
            a = params(1)
            print(a)
            i += 2
        elif o == 5: # jump if true
            a, b = params(2)
            if a != 0:
                i = b
            else:
                i += 3
        elif o == 6: # jump if false
            a, b = params(2)
            if a == 0:
                i = b
            else:
                i += 3
        elif o == 7: # less than
            a, b, c = params(2, 1)
            p[c] = int(a<b)
            i += 4
        elif o == 8: # equals
            a, b, c = params(2, 1)
            p[c] = int(a==b)
            i += 4
        elif o == 99: # exit
            break
        else:
            assert False, "unknown op %s" % o

prog = from_stdin()
print(prog)

run(prog, 5)
