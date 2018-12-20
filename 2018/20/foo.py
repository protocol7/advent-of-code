import sys

sys.setrecursionlimit(10000)

class Node():
    def __init__(self, parent):
        self.parent = parent
        self.c = {}

rev = {"N": "S", "S": "N", "W": "E", "E": "W"}

def w(rr, start):
    node = start
    while rr:
        c = rr.pop(0)
        if c == "(" or c == "^":
            w(rr, node)
        elif c ==")" or c == "$":
            return
        elif c == "|":
            node = start
        else:
            if node.c.get(c):
                node = node.c[c]
            elif node.parent and node.parent.c.get(rev[c]) == node:
                node = node.parent
            else:
                n = Node(node)
                node.c[c] = n
                node = n

def l(node, doors, max_doors, rooms):
    max_doors = max(max_doors, doors)
    for child in node.c.itervalues():
        md, rooms = l(child, doors + 1, max_doors, rooms)
        max_doors = max(max_doors, md)

    if doors >= 1000:
        rooms += 1
    return max_doors, rooms

inp = sys.stdin.read().strip()

root = Node(None)

w(list(inp), root)

max_doors, rooms = l(root, 0, 0, 0)
print(max_doors, rooms)
