import sys

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

d = {
    ")": "(",
    "]": "[",
    "}": "{",
}

def balanced(x):
    stack = []
    for c in x:
        if c in "([{":
            stack.append(c)
        elif c in d:
            if not stack:
                return False

            other = stack.pop()
            if other != d[c]:
                return False
            
    return not stack

print(sum(balanced(x) for x in xs))