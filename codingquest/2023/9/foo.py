import sys

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

class Node:
    def __init__(self, v):
        self.v = v
        self.a = None
        self.b = None

root = Node(xs[0])
for x in xs[1:]:
    cur = root

    while True:
        if x < cur.v:
            if cur.a:
                cur = cur.a
            else:
                cur.a = Node(x)
                break
        else:
            if cur.b:
                cur = cur.b
            else:
                cur.b = Node(x)
                break


def depth(n):
    if n is None:
        return 0
    return 1 + max(depth(n.a), depth(n.b))

nodes = [root]

max_width = 0
while nodes:
    max_width = max(max_width, len(nodes))

    nodes = [n.a for n in nodes if n.a] + [n.b for n in nodes if n.b]

print(max_width * depth(root))