import sys

p = list(map(int, sys.stdin))

for a in p:
    for b in p:
        for c in p:
            if a + b + c == 2020:
                print(a*b*c)
                sys.exit()