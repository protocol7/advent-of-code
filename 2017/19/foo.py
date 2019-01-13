import sys

def parse(line):
    return line

m = list(sys.stdin)

x = m[0].index("|")
y = 0
dx, dy = 0, 1

passed = []
steps = 0

while True:
    c = m[y][x]
    if c == "+":
        for nx, ny in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            xx = x + nx
            yy = y + ny
            if xx < 0 or yy < 0 or xx >= len(m[0]) or yy >= len(m) or m[yy][xx] == " ":
                continue

            if (-nx, -ny) != (dx, dy):
                dx, dy = nx, ny
                break
    elif c == " ":
        # done
        break
    elif c.isalpha():
        passed.append(c)

    x += dx
    y += dy
    steps += 1

print("".join(passed))
print(steps)
