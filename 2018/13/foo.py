import sys

def parse_line(line, y):
    row = ""
    carts = list()
    for x, pos in enumerate(line):
        if pos == ">" or pos == "<":
            carts.append((pos, x, y, 0))
            row += "-"
        elif pos == "^" or pos == "v":
            carts.append((pos, x, y, 0))
            row += "|"
        else:
            row += pos
    return row, carts

def parse(lines):
    rows = list()
    carts = list()
    for y, line in enumerate(lines):
        row, cs = parse_line(line, y)
        rows.append(row)
        carts.extend(cs)
    return rows, carts

def next_coord(pos, x, y):
    if pos == ">":
        x += 1
    elif pos == "<":
        x -= 1
    elif pos == "^":
        y -= 1
    elif pos == "v":
        y += 1
    return x, y

def next_dir(cur, turn, path):
    n = cur
    t = turn
    if path == "+":
        t = next_turn(turn)
        if cur == ">":
            if turn == 0:
                n = "^"
            elif turn == 1:
                n = ">"
            else:
                n = "v"
        elif cur == "<":
            if turn == 0:
                n = "v"
            elif turn == 1:
                n = "<"
            else:
                n = "^"
        elif cur == "^":
            if turn == 0:
                n = "<"
            elif turn == 1:
                n = "^"
            else:
                n = ">"
        elif cur == "v":
            if turn == 0:
                n = ">"
            elif turn == 1:
                n = "v"
            else:
                n = "<"
    elif path == "/":
        if cur == "^":
            n = ">"
        elif cur == "<":
            n = "v"
        elif cur == ">":
            n = "^"
        elif cur == "v":
            n = "<"
    elif path == "\\":
        if cur == "^":
            n = "<"
        elif cur == "<":
            n = "^"
        elif cur == ">":
            n = "v"
        elif cur == "v":
            n = ">"

    return n, t

def next_turn(turn):
    return (turn + 1) % 3

paths, carts = parse(sys.stdin)

done = False
while not done:
    carts = sorted(carts, key=lambda c: (c[2], c[1]))
    for i, (direction, x, y, turn) in enumerate(carts):
        x, y = next_coord(direction, x, y)

        # collision?
        if (x, y) in [(ox, oy) for _, ox, oy, _ in carts]:
            print("%s,%s" % (x, y))
            done = True
            break

        direction, turn = next_dir(direction, turn, paths[y][x])

        carts[i] = (direction, x, y, turn)
