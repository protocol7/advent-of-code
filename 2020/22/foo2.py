import sys

def parse(xs):
    return list(map(int, xs.split()[2:]))

a, b = map(parse, sys.stdin.read().split("\n\n"))

def game(a, b):
    seen = set()

    while a and b:
        key = (tuple(a), tuple(b))
        if key in seen:
            # a wins
            return True, a, b

        seen.add(key)

        x = a[0]
        a = a[1:]
        y = b[0]
        b = b[1:]

        if x <= len(a) and y <= len(b):
            a_won, _, _ = game(a[:x], b[:y])
        else:
            a_won = x > y

        if a_won:
            a = a + [x, y]
        else:
            b = b + [y, x]

    return bool(a), a, b


_, a, b = game(a, b)

print(sum((i+1) * x for i, x in enumerate(reversed(max(a, b)))))