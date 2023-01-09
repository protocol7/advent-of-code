from itertools import combinations

ds = [{
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
}]

for a, b in combinations("ABCD", 2):
    nds = []

    # a wins
    for d in ds:
        nd = dict(d)
        nd[a] += 3
        nds.append(nd)

    # b wins
    for d in ds:
        nd = dict(d)
        nd[b] += 3
        nds.append(nd)

    # even
    for d in ds:
        nd = dict(d)
        nd[a] += 1
        nd[b] += 1
        nds.append(nd)

    ds = nds

ds = set(tuple(sorted(d.values())) for d in ds)

ds = [d for d in ds if len(set(d)) == len(d)]

print(len(ds))