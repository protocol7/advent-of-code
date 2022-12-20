import sys

def parse(line):
    return int(line.strip())

xx = list(map(parse, sys.stdin))

for part, multiplier in ((1, 1), (10, 811589153)):
    xs = [(n * multiplier, i) for i, n in enumerate(xx)]
  
    for _ in range(part):
        for move in range(len(xs)):
            # find the next to move
            i = [oi for _, oi in xs].index(move)

            n, oi = xs.pop(i)

            ni = (i + n) % len(xs)

            xs.insert(ni, (n, oi))

        i = [n for n, _ in xs].index(0)

    s = 0
    for y in (1000, 2000, 3000):
        s += xs[(y + i) % (len(xs))][0]
    print(s)
