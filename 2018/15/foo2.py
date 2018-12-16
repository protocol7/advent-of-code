import sys
from copy import deepcopy

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

def attack(m, c, x, y, elf_power):
    targets = list()
    for ex, ey in adjecent(x, y):
        c2 = m[ey][ex]
        if isinstance(c2, Player) and c.enemy(c2):
            targets.append((c2, ex, ey))


    if targets:
        targets.sort(key=lambda (target, tx, ty): (target.p, ty, tx))

        target, tx, ty = targets[0]
        power = 3
        if c.t == "E":
            power = elf_power
        target.p -= power
        if target.p < 1:
            m[ty][tx] = Open()

def remains(m):
    elfs = 0
    goblins = 0
    elf_count = 0
    for row in m:
        for c in row:
            if isinstance(c, Player):
                if c.t == "G":
                    goblins += c.p
                elif c.t == "E":
                    elfs += c.p
                    elf_count += 1
    return elfs, goblins, elf_count

def is_remains(m):
    e, g, _ = remains(m)
    return e*g > 0

def fight(m, elf_power, start_elfs):
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
                        attack(m, c, x, y, elf_power)
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

                            attack(m, c, sx, sy, elf_power)

                            # are we done now?
                            if not is_remains(m):
                                done = True
                                break

        elfs, goblins, elf_count = remains(m)

        # did an elf die?
        if elf_count < start_elfs:
            return False
        elif goblins == 0:
            # elves won!
            rounds = r
            if done:
                rounds -= 1
            print(rounds*elfs)
            return True

m = []
for line in sys.stdin:
    m.append([parse(c) for c in line.strip()])

_, _, start_elfs = remains(m)
for elf_power in range(3, 100):
    if fight(deepcopy(m), elf_power, start_elfs):
        break
