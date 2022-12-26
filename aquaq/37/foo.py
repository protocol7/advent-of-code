import sys
from collections import *
from itertools import *
from util import *

def parse(line):
    line = line.strip()

    word = line.split(",")[0]
    return word, ints(line)

xs = list(map(parse, sys.stdin))

words = set()
with open("words.txt") as f:
    for word in f:
        word = word.strip()
        if len(word) == 5:
            words.add(word)

def matches(guess, results, word):
    # do all twos
    for i, (g, r) in enumerate(zip(guess, results)):
        if r == 2:
            # must have g in the right position
            if word[i] != g:
                return False
            else:
                # mark as matched
                word = word[:i] + "." + word[i+1:]

    # do all ones
    for i, (g, r) in enumerate(zip(guess, results)):
        if r == 1:
            # must have g in some position, but not this

            if g not in word or word[i] == g:
                return False
            else:
                # mark as matched
                ix = word.index(g)
                word = word[:ix] + "." + word[ix+1:]

    # do all zeros
    for i, (g, r) in enumerate(zip(guess, results)):
        if r == 0:
            # must not have g in word
            if g in word:
                return False

    return True

assert     matches("papyl", [0, 2, 0, 0, 0], "xaxxx")
assert not matches("papyl", [0, 2, 0, 0, 0], "xxxxx")
assert     matches("papyl", [0, 2, 0, 2, 0], "xaxyx")

assert     matches("papal", [0, 2, 0, 0, 0], "xaxxx")
assert not matches("papal", [0, 2, 0, 0, 0], "xaxxa")

assert     matches("papal", [0, 2, 0, 1, 0], "xaxxa")

assert     matches("marry", [2, 2, 1, 0, 0], "major")

assert not matches("manor", [2, 2, 0, 2, 2], "manor")

assert     matches("egger", [2, 0, 2, 2, 2], "eager")


ws = set(words)
correct = []
for guess, results in xs:
    ws = set(word for word in ws if matches(guess, results, word))

    if len(ws) == 1:
        # found a word
        correct.append(item(ws))
        ws = set(words)

for hack in sorted(ws):
    s = 0
    for x in flatten(correct) + list(hack):
        s += ord(x) - ord("a")

    print("With " + hack + ": " + str(s))

# with "right" turned out to be correct