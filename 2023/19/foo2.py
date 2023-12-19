import sys
from util import msplit
from math import prod

def parse_a(line):
    return msplit(line.strip(), "{,}")

a, _ = sys.stdin.read().strip().split("\n\n")

a = list(map(parse_a, a.splitlines()))

rules = {}
for x in a:
    rules[x[0]] = x[1:]

def foo(rule, step_index, xs) -> int:
    if rule == "A":
        return prod(x[1] - x[0] + 1 for x in xs.values())
    elif rule == "R":
        return 0
    
    step = rules[rule][step_index]

    def clone_dict(d, what, value):
        c = dict(d)
        c[what] = value
        return c

    if ":" in step:
        # handle rule
        pred, next = step.split(":")
        what, lim = msplit(pred, "<>")
        lim = int(lim)

        lo, hi = xs[what]
        assert hi > lim
        assert lo < lim

        if ">" in pred:
            t = foo(next, 0, clone_dict(xs, what, (lim + 1, hi)))
            f = foo(rule, step_index + 1, clone_dict(xs, what, (lo, lim)))
        else:
            t = foo(next, 0, clone_dict(xs, what, (lo, lim - 1)))
            f = foo(rule, step_index + 1, clone_dict(xs, what, (lim, hi)))

        return t + f
                    
    else:
        # handle fallback
        return foo(step, 0, xs)

print(foo("in", 0, {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}))
