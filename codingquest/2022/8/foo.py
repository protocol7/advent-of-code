import sys
from itertools import cycle

def parse(line):
    return line.strip()


CS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,;:?! '()"
SECRET = cycle("Roads? Where We're Going, We Don't Need Roads.")

ct = sys.stdin.read().strip()

clear = ""
for c, s in zip(ct, SECRET):
    if not c in CS:
        clear += c
    else:
        si = CS.find(s) + 1
        ci = CS.find(c)

        cc = CS[(ci - si) % len(CS)]

        clear += cc

print(clear)
