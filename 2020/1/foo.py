import sys

p = list(map(int, sys.stdin))

for a in p:
    for b in p:
        if a + b == 2020:
            print(a*b)
            sys.exit()