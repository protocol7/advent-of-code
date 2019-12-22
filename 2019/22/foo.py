import sys

def new_stack(cards, _):
    return cards[::-1]

def cut(cards, i):
    return cards[i:] + cards[:i]

def incr(cards, i):
    c = iter(cards)
    out = [0] * len(cards)
    for x in range(len(cards)):
        xx = (x * i) % len(cards)
        out[xx] = next(c)
    return out

def parse(line):
    line = line.strip()
    if line == "deal into new stack":
        return (new_stack, 0)
    elif line.startswith("deal with increment"):
        return (incr, int(line.split()[-1]))
    elif line.startswith("cut"):
        return (cut, int(line.split()[-1]))

shuf = map(parse, sys.stdin)
cards = list(range(int(sys.argv[1])))

for s, i in shuf:
    cards = s(cards, i)

print(cards.index(2019))
