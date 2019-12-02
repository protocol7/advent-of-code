import sys

p = map(int, list(sys.stdin)[0].strip().split(","))
p[1] = 12
p[2] = 2

i = 0

while True:
    o = p[i]
    print(i, o)

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

print(p[0])

