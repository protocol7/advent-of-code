import sys

def parse(c):
    if c == "G" or c == "E":
        return Player(c)
    elif c == "#":
        return Wall()
    elif c == ".":
        return Open()
    else:
        print("error " + c)

class Player:
    def __init__(self, t):
        self.t = t
        self.p = 200

    def enemy(self, p):
        return self.t != p.t

class Wall:
    pass

class Open:
    pass

def adjecent(x, y):
    return [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]

def find_enemies(m, p):
    inrange = list()
    for y, row in enumerate(m):
        for x, c in enumerate(row):
            if isinstance(c, Player) and p != c:
                if p.t != c.t:
                    inrange.append((x, y))
    return inrange

def find_paths(m, x, y, targets):
    paths = set()
    open = list([((x, y),)])
    visited = set([(x, y)])

    while open and not paths:
        new_open = set()
        for p in open:
            px, py = p[-1]
            for cx, cy in adjecent(px, py):
                if (cx, cy) in visited:
                    pass
                elif (cx, cy) in targets:
                    paths.add(p + tuple([(cx, cy)]))
                elif isinstance(m[cy][cx], Open):
                    new_open.add(p + tuple([(cx, cy)]))
                    visited.add((cx, cy))
        new_open = list(new_open)
        new_open.sort(key=lambda p: (p[1][1], p[1][0]))
        open = new_open
    return list(paths)

def can_attach(m, c, x, y):
    for ex, ey in adjecent(x, y):
        c2 = m[ey][ex]
        if isinstance(c2, Player) and c.enemy(c2):
            return True
    return False

def attack(m, c, x, y):
    targets = list()
    for ex, ey in adjecent(x, y):
        c2 = m[ey][ex]
        if isinstance(c2, Player) and c.enemy(c2):
            targets.append((c2, ex, ey))


    if targets:
        targets.sort(key=lambda (target, tx, ty): (target.p, ty, tx))

        target, tx, ty = targets[0]
        target.p -= 3
        if target.p < 1:
            m[ty][tx] = Open()

def remains(m):
    elfs = 0
    goblins = 0
    for row in m:
        for c in row:
            if isinstance(c, Player):
                if c.t == "G":
                    goblins += c.p
                elif c.t == "E":
                    elfs += c.p
    return elfs, goblins

def is_remains(m):
    e, g = remains(m)
    return e*g > 0

m = []
for line in sys.stdin:
    m.append([parse(c) for c in line.strip()])

for r in range(1, 1000):
    turned = set()

    done = False
    for y, row in enumerate(m):
        new_row = list()
        for x, c in enumerate(row):
            if not done and isinstance(c, Player) and c not in turned:
                # are we already done?
                if not is_remains(m):
                    done = True
                    break

                turned.add(c)
                if can_attach(m, c, x, y):
                    attack(m, c, x, y)
                else:
                    # move
                    inrange = find_enemies(m, c)
                    paths = find_paths(m, x, y, inrange)
                    if paths:
                        paths.sort(key=lambda p: (p[-1][1], p[-1][0], p[1][1], p[1][0]))

                        # next step
                        sx, sy = paths[0][1]

                        m[sy][sx] = c
                        m[y][x] = Open()

                        attack(m, c, sx, sy)

                        # are we done now?
                        if not is_remains(m):
                            done = True
                            break

    elfs, goblins = remains(m)

    if elfs * goblins ==  0:
        rounds = r
        # did we end early, don't count this round
        if done:
            rounds -= 1
        print(rounds * max(goblins, 1) * max(elfs, 1))
        break
