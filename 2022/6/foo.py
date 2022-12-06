import sys

xs = sys.stdin.read().strip()

for o in (4, 14):
    for i in range(len(xs)):
        s = xs[i:i+o]

        if len(set(s)) == o:
            print(i+o)
            break
