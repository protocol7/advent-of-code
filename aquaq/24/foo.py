import sys
from collections import *
from itertools import *
from util import *

chars, bits = sys.stdin.read().strip().split("\n")

c = Counter(chars)

class Node:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def value(self):
        return self.a.value() + self.b.value()

    def frequency(self):
        return self.a.frequency() + self.b.frequency()

    def __repr__(self) -> str:
        return "'%s', %s" % (self.value(), self.frequency())

class Leaf:
    def __init__(self, val, freq):
        self.val = val
        self.freq = freq

    def value(self):
        return self.val

    def frequency(self):
        return self.freq

    def __repr__(self) -> str:
        return "'%s':%s" % (self.value(), self.frequency())

# The first two elements at each point are merged together into a single node with two direct subnodes - 
# the elements are placed side-by-side (whether full tree or single node) and both are connected directly 
# to a shared parent node above. This new tree has a total weight of the sum of all letters in it. 
# The tree is then re-inserted into the above set of nodes, and the set sorted based on the total weight 
# of each node and its subnodes. In the case of a tie, new trees are inserted at the bottom of the group 
# of their tied weights (e.g. a group "ab" with weight 10 would go into a node group "c:7 f:10 g:10 l:11" 
# after the "g)"


nodes = [Leaf(a, b) for a, b in c.most_common()]

nodes = sorted(nodes, key=lambda n: (n.freq, n.val))

while len(nodes) > 1:
    # take first two nodes
    a = nodes.pop(0)
    b = nodes.pop(0)
    nn = Node(a, b)

    # find first in nodes with higher weight
    index = None
    for i, n in enumerate(nodes):
        if n.frequency() > nn.frequency():
            index = i
            break

    if index is not None:
        nodes.insert(index, nn)
    else:
        nodes.append(nn)

root = item(nodes)

def visit(node, code, codes):
    if type(node) == Leaf:
        codes[code] = node.value()
    else:
        visit(node.a, code + "0", codes)
        visit(node.b, code + "1", codes)

codes = {}
visit(root, "", codes)

cur = ""
bits = list(bits)
s = ""
while bits:
    cur += bits.pop(0)

    if cur in codes:
        s += codes[cur]
        cur = ""

print(s)
