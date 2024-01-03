import sys
from collections import defaultdict, deque
import graphviz

def parse(line):
    a, b = line.strip().split(": ")
    return a, b.split()

xs = list(map(parse, sys.stdin))

graph = defaultdict(set)

for a, bs in xs:
    for b in bs:
        graph[a].add(b)
        graph[b].add(a)

dot = graphviz.Graph(engine='neato')

for n in graph.keys():
    dot.node(n)

seen = set()
for a, bs in graph.items():
    for b in bs:
        if (a, b) not in seen:
            dot.edge(a, b)
        seen.add((b, a))

#dot.render("graph", view=True)

# manually identify edges to cut
cut = [
    ("htj", "pcc"),
    ("dlk", "pjj"),
    ("htb", "bbg"),
]

for a, b in cut:
    graph[a].remove(b)
    graph[b].remove(a)

def count_connected(graph, start):
    q = deque([start])
    seen = set()

    while q:
        a = q.popleft()

        if a in seen:
            continue
        seen.add(a)

        for b in graph[a]:
            q.append(b)

    return len(seen)

a, b = cut[0]
na = count_connected(graph, a)
nb = count_connected(graph, b)
print(na * nb)
