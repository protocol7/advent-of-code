import sys

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

# part 1
g = ""
for i in range(len(xs[0])):
    ones = sum(int(x[i]) for x in xs)

    g += str(int(ones > len(xs) / 2))

# e is the inverse of g, lazy xor
e = "".join("1" if x == "0" else "0" for x in g)

def m(g, e):
    return int(g, 2) * int(e, 2)

print(m(g, e))


# part 2
def find(xs, most):
    for i in range(len(xs[0])):
        ones = sum(int(x[i]) for x in xs)

        if most:
            # is 1 the most common, default to 1 if even
            f = str(int(ones >= len(xs) / 2))
        else:
            # is 1 the least common, default to 0 if even
            f = str(int(ones < len(xs) / 2))
            
        xs = list(filter(lambda x: x[i] == f, xs))

        if len(xs) == 1:
            return xs[0]

print(m(find(xs, True), find(xs, False)))