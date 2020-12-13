import sys

_, b = sys.stdin.readlines()

xs = [(int(x), i) for i, x in enumerate(b.split(",")) if x != "x"]

c = 0  # current
m = 1  # multiplier. input values are prime so we can just use the product of those we've matched

for n, o in xs:  # bus-id, offset
    # while c is not a multiplier at the right offset, keep iterating on c
    while (c + o) % n != 0:
        c += m

    m *= n

print(c)