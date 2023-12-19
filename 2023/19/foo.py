import sys
from util import msplit, pairs

def parse_a(line):
    return msplit(line.strip(), "{,}")

def parse_b(line):
    bs = pairs(msplit(line.strip(), "{,}="))
    return {a: int(b) for a, b in bs}


a, b = sys.stdin.read().strip().split("\n\n")

a = list(map(parse_a, a.splitlines()))
rules = {}
for x in a:
    rules[x[0]] = x[1:]

b = list(map(parse_b, b.splitlines()))

def apply_rule(rule, x):
    for step in rule:
        if ":" in step:
            pred, out = step.split(":")
            what, lim = msplit(pred, "<>")
            cmp = int.__gt__ if ">" in pred else int.__lt__
            lim = int(lim)

            if cmp(x[what], lim):
                return out
        else:
            return step

def apply_rules(rules, rule, x):
    while True:
        rule = apply_rule(rules[rule], x)

        if rule == "A":
            return True
        elif rule == "R":
            return False

accepted = 0
for x in b:
    if apply_rules(rules, "in", x):
        accepted += sum(x.values())

print(accepted)
