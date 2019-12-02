import sys

prog = map(int, list(sys.stdin)[0].strip().split(","))

def run(prog, noun, verb):
    p = prog[:]
    p[1] = noun
    p[2] = verb

    i = 0

    while True:
        o = p[i]

        if o == 1:
            a = p[i+1]
            b = p[i+2]
            c = p[i+3]
            p[c] = p[a] + p[b]
            i += 4
        elif o == 2:
            a = p[i+1]
            b = p[i+2]
            c = p[i+3]
            p[c] = p[a] * p[b]
            i += 4
        elif o == 99:
            break
        else:
            assert False
    return p[0]


for n in range(0, 100):
    for v in range(0, 100):
        out = run(prog, n, v)
        if out == 19690720:
            print(n * 100 + v)
