import sys
from itertools import islice

def next(s):
    s = list(s)
    s.reverse()
    for i, c in enumerate(s):
        if c == "z":
            s[i] = "a"
        else:
            s[i] = chr(ord(c) + 1)
            s.reverse()
            return "".join(s)

def valid1(s):
    for a, b, c in zip(s, s[1:], s[2:]):
        if ord(a) + 2 == ord(b) + 1 == ord(c):
            return True
    return False

def valid2(s):
    for c in "iol":
        if c in s:
            return False
    return True

def valid3(s):
    pairs = 0
    i = 0
    while i < len(s) - 1:
        a, b = s[i], s[i + 1]
        if a == b:
            pairs += 1
            i += 1
        i += 1
    return pairs >= 2

def valid(s):
    return valid1(s) and valid2(s) and valid3(s)

def gen(start):
    s = start
    while True:
        s = next(s)
        while not valid(s):
            s = next(s)
        yield s

inp = sys.argv[1]
print(list(islice(gen(inp), 2)))
