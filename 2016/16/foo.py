import sys

def gen(start, length):
    a = start
    while len(a) < length:
        b = a
        b = b[::-1]
        b = "".join(["1" if x == "0" else "0" for x in b])
        a = a + "0" + b
    return a[:length]

def checksum(s):
    c = cs(s)
    while len(c) % 2 == 0:
        c = cs(c)
    return c

def cs(s):
    x = ""
    for i in range(0, len(s), 2):
        c1 = s[i]
        c2 = s[i+1]
        if c1 == c2:
            x += "1"
        else:
            x += "0"
    return x


init = sys.argv[1]
size = int(sys.argv[2])

print(checksum(gen(init, size)))
