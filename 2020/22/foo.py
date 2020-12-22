import sys

def parse(xs):
    return list(map(int, xs.split()[2:]))

a, b = map(parse, sys.stdin.read().split("\n\n"))

def score(a, b):
    print(sum((i+1) * x for i, x in enumerate(reversed(max(a, b)))))

while a and b:
    x = a[0]
    a = a[1:]
    y = b[0]
    b = b[1:]

    if x > y:
        a = a + [x, y]
    else:
        b = b + [y, x]

score(a, b)