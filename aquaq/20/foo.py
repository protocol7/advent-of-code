import sys
from collections import *
from itertools import *
from util import *


xs = sys.stdin.read().strip().split()

wins = 0
scores = [0]
for x in xs:
    if x in "JQK":
        s = [10]
    elif x == "A":
        s = [1, 11]
    else:
        s = [int(x)]

    ns = []
    for ss in s:
        for score in scores:
            ns.append(score + ss)

    scores = ns
    
    if 21 in scores:
        wins += 1
        scores = [0]
    elif all(map(lambda i: i > 21, scores)):
        scores = [0]

print(wins)