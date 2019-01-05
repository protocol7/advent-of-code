import sys
from collections import Counter

discs = {}
for line in sys.stdin:
    line = line.split()
    w = int(line[1].strip("()"))
    children = set()
    if len(line) > 3:
        children = set([x.strip(",") for x in line[3:]])

    discs[line[0]] = (w, children)

all_children = set()
for _, c in discs.values():
    all_children.update(c)
root = list(set(discs.keys()).difference(all_children))[0]
print(root)

# part 2

def w(d):
    d = discs[d]
    ww = d[0]
    for c in d[1]:
        ww += w(c)[0]
    return ww, d[0]


def balance(n, depth):
    d = discs[n]
    ws = []
    for c in d[1]:
        x, y = w(c)
        ws.append((x, y))
        if not balance(c, depth + 1):
            return False

    if ws:
        c = Counter()
        for tw, _ in ws:
            c[tw] += 1
        # is there more than one weight
        if len(c) > 1:
            w1, w2 = [x for x, _ in c.most_common()]
            delta = w2 - w1

            for tw, dw in ws:
                if tw == w2:
                    # adjust the different one
                    print(dw - delta)

            return False

    return True

balance(root, 1)
