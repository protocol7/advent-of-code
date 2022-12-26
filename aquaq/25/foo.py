import sys
from collections import *
from itertools import *
from util import *
import datetime

msgs = sys.stdin.read().strip().split("\n            \n")

alpha = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
}
alpha = {v:k for k, v in alpha.items()}

for msg in msgs:
    msg = msg.split("\n")


    def parse(ts):
        return datetime.datetime.strptime(ts + "0", "%H:%M:%S.%f")

    msg = [parse(ts) for ts in msg]

    deltas = []
    for a, b in zip(msg, msg[1:]):
        deltas.append(int((b - a) / datetime.timedelta(milliseconds=1)))
    
    dot = min(deltas)
    dash = dot * 3
    word = dot * 7

    spacing = False
    cur = ""
    morse = []
    for delta in deltas:
        if not spacing:
            if delta == dot:
                cur += "."
            elif delta == dash:
                cur += "-"

            spacing = True
        else:
            if delta == dot:
                pass
            elif delta == dash:
                morse.append(cur)
                cur = ""
            elif delta == word:
                morse.append(cur)
                cur = ""
                morse.append(" ")

            spacing = False

    morse.append(cur)

    s = ""
    for m in morse:
        if m == " ":
            s += " "
        else:
            s += alpha[m]
    print(s)

# the first letter of the answer is p
# the second character is q and the first letter is still p
# the third alphanumeric element is r and the second letter is now a
# the fourth is i
# test line please ignore zxcociquuzeotrwnqyiewmnaxzxcvl
# the final glyph is the letter following r in the alphabet

# paris