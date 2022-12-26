import sys
from collections import *
from itertools import *
from util import *
from math import sqrt

xs = sys.stdin.read()

xs = xs[:-1]

words = []
with open("words.txt") as f:
    for word in f:
        word = word.strip()
        words.append(word)

# 2 2 2 2 181 are the factors of the length of the input
cipher_words = set(filter(lambda w: len(w) in (2, 4, 8, 16, 32), words))

def code_mapping(word):
    d = sorted(enumerate(word), key=lambda w: w[1])
    return {i: o for i, (o, _) in enumerate(d)}

for word in cipher_words:
    mapping = code_mapping(word)
    cs = chunks(xs, len(xs) // len(word))

    out = [None] * len(cs)

    for i, c in enumerate(cs):
        out[mapping[i]] = c

    out = join(flatten(transpose(out)))

    # check the three first if they are real words
    tokens = out.split(" ")[:3]

    if all(t.lower() in words for t in tokens):
        print(word, out)
        break