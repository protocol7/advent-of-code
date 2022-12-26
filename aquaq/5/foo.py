import sys

xs = sys.stdin.read().strip()

# For U
# top = front
# front = 7 - top

# For D
# front = top
# top = 7 - front

# For L
# Left = front
# Front = 7 - left

# For R
# Front = Left
# Left = 7 - Front

dices = [(1, 3, 2), (1, 2, 3)]

s = 0
for mi, m in enumerate(xs):
    for i, (front, top, left) in enumerate(dices):

        if m == "L":
            front, left = 7 - left, front
        elif m == "R":
            front, left = left, 7 - front
        elif m == "U":
            top, front = front, 7 - top
        elif m == "D":
            front, top = top, 7 - front

        dices[i] = (front, top, left)

    if dices[0][0] == dices[1][0]:
        s += mi

print(s)