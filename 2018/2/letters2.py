import sys
from collections import defaultdict

def find_distance_one(word, words):
    for w in words:
        common = "".join(map(lambda (x, y): x, filter(lambda (x, y): x == y, zip(word, w))))
        if len(common) == len(word) - 1:
            return common

words = list(sys.stdin)

print(filter(lambda w: w, map(lambda w: find_distance_one(w, words), words))[0])
