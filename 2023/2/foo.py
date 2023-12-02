import sys

def parse(line):
    a, b = line.split(":")
    
    a = int(a.split()[1])
    bs = [b.split(",") for b in b.split(";")]

    return a, bs

xs = list(map(parse, sys.stdin))

# 12 red cubes, 13 green cubes, and 14 blue cubes

t = 0
for i, bs in xs:
    p = True
    for b in bs:
        for a in b:
            x, y = a.split()
            x = int(x)

            if y == "red" and x > 12:
                p = False
            if y == "blue" and x > 14:
                p = False
            if y == "green" and x > 13:
                p = False

    if p:
        t += i

print(t)
