import sys

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

cs = set(xs[0])

words = " ".join(xs).split()
print(len({word for word in words if len(set(word)) == len(set(word) & cs)}))

