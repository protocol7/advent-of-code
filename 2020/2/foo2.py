import sys
from util import *

def f(a, b, c, _, p):
    return (p[a-1] == c) != (p[b-1] == c)

ps = map(lambda l: intify(msplit(l, "-: ")), sys.stdin)
print(ilen(filter(lambda x: f(*x), ps)))