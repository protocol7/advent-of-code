import sys

def parse(line):
    s, e = [int(i) for i in line.split("-")]
    return (s, e)

rules = map(parse, sys.stdin)
rules.sort()

def merge(rules):
    index = 0
    while index + 1 < len(rules):
        s1, e1 = rules[index]
        s2, e2 = rules[index + 1]

        if e1 + 1 >= s2:
            rules[index] = (min(s1, s2), max(e1, e2))
            del rules[index + 1]
        else:
            index += 1
    return rules

rules = merge(rules)

print(rules[0][1] + 1)

# part 2
white = rules[0][0]

for (s1, e1), (s2, e2) in zip(rules, rules[1:]):
    white += s2 - e1 - 1

white += 4294967295 - rules[-1][1]

print(white)
