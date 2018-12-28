import sys
from copy import copy
from heapq import heappush, heappop

class State():
    def __init__(self, player_hp, boss_hp, mana):
        self.player_hp = player_hp
        self.boss_hp = boss_hp
        self.shield = 0
        self.poison = 0
        self.recharge = 0
        self.mana = mana
        self.used = 0

def effects(s, indent):
    if s.poison:
        s.boss_hp -= 3
        s.poison -= 1
    if s.recharge:
        s.mana += 101
        s.recharge -= 1
    if s.shield:
        s.shield -= 1
        return 7
    else:
        return 0

def turn(state, costs, indent):
    # player

    if hard:
        state.player_hp -= 1
        if state.player_hp <= 0:
            return

    effects(state, indent)
    if state.boss_hp <= 0:
        # done, player won
        costs.append(state.used)
        return

    avail_magic = filter(lambda (_, c): c <= state.mana, magic)
    for m, c in avail_magic:
        new_state = copy(state)

        if m == "missile":
            new_state.boss_hp -= 4
        elif m == "poison" and not new_state.poison:
            new_state.poison = 6
        elif m == "shield" and not new_state.shield:
            new_state.shield = 6
        elif m == "drain":
            new_state.boss_hp -= 2
            new_state.player_hp += 2
        elif m == "recharge" and not new_state.recharge:
            new_state.recharge = 5
        else:
            continue

        new_state.mana -= c
        new_state.used += c

        if new_state.boss_hp <= 0:
            # done, player won
            costs.append(new_state.used)
            continue

        # boss
        armor = effects(new_state, indent)
        if new_state.boss_hp <= 0:
            # done, player won
            costs.append(new_state.used)
            continue

        damage = max(boss_damage - armor, 1)
        new_state.player_hp -= damage

        if new_state.player_hp <= 0:
            # player dead
            continue

        heappush(queue, (new_state.used, new_state))

magic = [("drain", 73), ("missile", 53), ("poison", 173), ("shield", 113), ("recharge", 229)]

hp = 50
mana = 500
boss_hp = int(sys.argv[1])
boss_damage = int(sys.argv[2])

hard = len(sys.argv) > 3

costs = [sys.maxint]
queue = []
heappush(queue, (0, State(hp, boss_hp, mana)))

while queue:
    c, state = heappop(queue)
    min_cost = min(costs)
    if c < min_cost:
        turn(state, costs, "")

print(min(costs))
