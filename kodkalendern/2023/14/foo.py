import sys

xs = sys.stdin.read().splitlines()

def extract(x):
    i = len(x) // 2
    return int(x[0]), int(x[i]), int(x[-1])

for i, (x, y) in enumerate(zip(xs, xs[1:])):
    a, _, b = extract(x)
    _, c, _ = extract(y)

    if a + b != c:
        print(i+1)
