import sys

s = 0
for x in sys.stdin:
    x = int(x)

    if x == 2:
        s += 2
        s *= 2
    elif x < 50:
        s += x
    else:
        s -= x

print(s)