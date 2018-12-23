import sys
import re

def rule1(s):
    return len(re.findall(r"([a-z]{2}).*\1", s)) >= 1

def rule2(s):
    return len(re.findall(r"([a-z])[a-z]\1", s)) >= 1

strings = list(sys.stdin)

strings = filter(rule1, strings)
strings = filter(rule2, strings)

print(len(strings))



