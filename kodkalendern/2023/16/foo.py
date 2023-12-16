import sys


def parse(line):
    line = line.strip()
    m = len(line) // 2

    a = list(map(int, line[:m][::-1]))
    b = int(line[m])
    c = list(map(int, line[m+1:]))
    return line, b, a, c


xs = list(map(parse, sys.stdin))

for n, s, x, y in xs:
    for a, b in zip(x, y):
        if a + b != s:
            print(n)
