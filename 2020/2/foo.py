import sys
from util import *

def f(a, b, c, _, p):
    return a <= p.count(c) <= b

ps = map(lambda l: intify(msplit(l, "-: ")), sys.stdin)
print(ilen(filter(lambda x: f(*x), ps)))