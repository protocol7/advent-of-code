import sys
from collections import defaultdict
from itertools import chain, imap

def flatmap(f, items):
    return chain.from_iterable(imap(f, items))

def parse(line):
    pass

inp = sys.stdin.read().strip()

print(inp.count("(") - inp.count(")"))
