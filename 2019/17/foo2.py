import sys
from intcode import *

prog = parse(sys.stdin)
ic = Intcode(prog, [])

m = dict()
x, y = 0, 0
droid = None

# get maze by running the program which outputs #, ., newlines and the robot
# direction in ascii
while True:
    o = ic.run()

    if o is None:
        break
    elif o == 10:
        y += 1
        x = 0
    else:
        if chr(o) == "^":
            droid = (x, y)
        m[(x, y)] = chr(o)
        x += 1

# table of directions if turning left and right from the key direction
turns = {
    (0, -1): [(-1, 0), (1, 0)],
    (0, 1): [(1, 0), (-1, 0)],
    (-1, 0): [(0, 1), (0, -1)],
    (1, 0): [(0, -1), (0, 1)],
        }

# find the path through the maze by walking forward as long as possible, then
# try to turn either left or right
def path(m, start):
    # the droid always starts up
    d = (0, -1)
    x, y = start
    path = []
    steps = 0
    while True:
        dx, dy = d
        nx = x + dx
        ny = y + dy
        c = m.get((nx, ny), ".")
        if c == "#":
            # go forward
            steps += 1
            x, y = nx, ny
        else:
            # we can't move further forward, add the number of steps we've
            # walked and then try to find a new direction
            path.append(steps)
            steps = 0

            turned = False
            for di, dd in enumerate(["L", "R"]):
                nd = turns[d][di]
                dx, dy = nd
                nx = x + dx
                ny = y + dy
                c = m.get((nx, ny), ".")
                if c == "#":
                    # turning worked
                    path.append(dd)
                    d = nd
                    turned = True
                    break

            # could not turn, we're done
            if not turned:
                return path


p = path(m, droid)

print(",".join([str(x) for x in p]))

# these were manually derived from p
a = "L,6,R,12,R,8"
b = "R,8,R,12,L,12"
c = "R,12,L,12,L,4,L,4"

main = "A,B,B,A,C,A,C,A,C,B"

inp = []
for x in [main, a, b, c, "n"]:
    inp += x
    inp.append(chr(10))

# convert to ascii intergers
inp = [ord(c) for c in inp]
inp_iter = iter(inp)

prog[0] = 2

ic = Intcode(prog, lambda: next(inp_iter))

while True:
    o = ic.run()

    if o == None:
        break
    else:
        if o > 256:
            print(o)
        else:
            # program prints output (including prompts for input)
            sys.stdout.write(chr(o))
            sys.stdout.flush()
