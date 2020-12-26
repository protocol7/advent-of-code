from collections import deque

g = {
    "1:1:22": ["2:1:-", "1:2:+"],
    "2:1:-" : ["1:1:22", "2:2:4", "3:1:9"],
    "3:1:9" : ["2:1:-", "3:2:-", "4:1:*"],
    "4:1:*" : ["3:1:9", "4:2:18"],
    "1:2:+" : ["1:1:22", "1:3:4", "2:2:4"],
    "2:2:4" : ["1:2:+", "2:1:-", "2:3:*", "3:2:-"],
    "3:2:-" : ["2:2:4", "3:1:9", "3:3:11", "4:2:18"],
    "4:2:18": ["3:2:-", "4:1:*", "4:3:*"],
    "1:3:4" : ["1:2:+", "1:4:*", "2:3:*"],
    "2:3:*" : ["1:3:4", "2:2:4", "2:4:8", "3:3:11"],
    "3:3:11": ["2:3:*", "3:2:-", "3:4:-", "4:3:*"],
    "4:3:*" : ["3:3:11", "4:2:18", "4:4:1"],
    "1:4:*" : ["1:3:4", "2:4:8"],
    "2:4:8" : ["1:4:*", "2:3:*", "3:4:-"],
    "3:4:-" : ["2:4:8", "3:3:11", "4:4:1"],
    "4:4:1" : ["3:4:-", "4:3:*"],
}

# type in the above manually, validate
assert not set(g.keys()) - set.union(*[set(x) for x in g.values()])
assert not set.union(*[set(x) for x in g.values()]) - set(g.keys())

start = "1:1:22"
end = "4:4:1"

def p(x):
    return x.split(":")[-1]

# evaluate in order. also tried using eval() but that wasn't accepted by the vault
def eval_exp(xs):
    assert len(xs) % 2 != 0

    v = int(p(xs[0]))
    for i in range(1, len(xs), 2):
        a = p(xs[i])
        b = int(p(xs[i+1]))

        if a == "+":
            v += b
        elif a == "*":
            v *= b
        elif a == "-":
            v -= b
        else:
            assert False

    return v

assert 78 == eval_exp(["1:1:22", "1:1:+", "1:1:4", "1:1:*", "1:1:3"])

def at_end(n, p):
    return n == end and len(p) % 2 == 1 and eval_exp(p) == 30


# graph is dict of node -> neighbours
# end is predicate function
# returns path from start to end
def bfs(graph, start, end):
    q = deque([[start]])
    seen = set()

    while q:
        path = q.popleft()
        v = path[-1]
        for n in graph[v]:
            if len(path) % 2 == 0 and n == path[-2]:
                # you're not allowed to walk to an operator and then back. without this check and the below you can find the shorter path 22 + 22 + 4 - 18 * 1
                continue
            elif n == "1:1:22":
                # for whatever reason it seems forbidden to go back to the starting position. found through trial and error
                continue

            p = path + [n]
            if end(n, p):
                return p

            q.append(p)

path = bfs(g, start, at_end)

print(" ".join(map(p, path)))