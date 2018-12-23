import sys
import re

def wovels(s):
    return len(re.findall("[aeiou]", s)) >= 3

def double(s):
    return len(re.findall(r"([a-z])\1", s)) >= 1

def block(s):
    return len(re.findall("ab|cd|pq|xy", s)) == 0


strings = list(sys.stdin)

strings = filter(wovels, strings)
strings = filter(double, strings)
strings = filter(block, strings)

print(len(strings))



