import sys
from collections import defaultdict
from itertools import chain, imap

def flatmap(f, items):
    return chain.from_iterable(imap(f, items))

inp = sys.stdin.read().strip()

escaped = False
garbage = False
depth = 0
score = 0
chars =  0
for c in inp:
    if escaped:
        escaped = False
    elif c == "!":
        escaped = True
    elif c == "<" and not garbage:
        garbage = True
    elif c == ">" and garbage:
        garbage = False
    elif c == "{" and not garbage:
        depth += 1
    elif c == "}" and not garbage:
        score += depth
        depth -= 1
    elif garbage:
        chars += 1

print(score)
print(chars)
