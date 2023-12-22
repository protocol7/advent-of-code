import sys
from util import chunks, ints

def parse(line):
    return chunks(ints(line.strip()), 3)

xs = list(map(parse, sys.stdin))

bricks = []
for a, b in xs:
    bricks.append([(x, y, z) for x in range(a[0], b[0] + 1) for y in range(a[1], b[1] + 1) for z in range(a[2], b[2] + 1)])


def pack(bricks):
    occupied = set()
    final_bricks = []

    n_fell = 0

    # pack from below by sorting by the lower z for each brick
    for brick in sorted(bricks, key=lambda b: b[0][2]):
        fell = False

        while brick[0][2] > 1:
            new_brick = [(x, y, z - 1) for x, y, z in brick]

            if any(c in occupied for c in new_brick):
                break

            brick = new_brick

            fell = True

        if fell:
            n_fell += 1

        final_bricks.append(brick)

        occupied.update(brick)

    return final_bricks, n_fell

bricks, _ = pack(bricks)

p1 = 0
p2 = 0
# try nuking one brick at a time and see if anything can now fall further
for i in range(len(bricks)):
    _, f = pack(bricks[:i] + bricks[i+1:])

    p1 += f == 0
    p2 += f

print(p1)
print(p2)
