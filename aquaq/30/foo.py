import sys
from functools import cache

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

m = {"0": "1", "1": "0"}

def segment(s, i):
    prefix = s[:i]
    suffix = s[i+1:]

    if prefix:
        # flip last
        prefix = prefix[:-1] + m[prefix[-1]]

    if suffix:
        # flip first
        suffix = m[suffix[0]] + suffix[1:]

    return prefix, suffix


@cache
def foo(s):
    if not s:
        # empty, we've won
        return True

    if int(s) == 0:
        # all zeros
        return False

    for i, c in enumerate(s):
        if c == "1":
            a, b = segment(s, i)

            if foo(a) and foo(b):
                return True

    return False

assert foo("11010")
assert foo("111") and foo("1")
assert not (foo("0") and foo("110"))

def firsts(s):
    out = 0
    for i, c in enumerate(s):
        if c == "1":
            a, b = segment(s, i)

            if foo(a) and foo(b):
                out += 1

    return out

assert firsts("00101011010") == 3
assert firsts("0111001111010001010000110000100") == 7
assert firsts("01011001111001011000110010011000011100110010") == 11
assert firsts("1110011011010000011011010011111001000111111010000100001110011101110011110000000110111010") == 0

s = 0
for i, x in enumerate(xs):
    print(i)
    f = firsts(x)
    s += f

print(s)