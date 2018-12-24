import sys
import re
from itertools import count
from copy import deepcopy

class Group():
    def __init__(self, army, units, points, immune, weak, damage, type, initiative):
        self.army = army
        self.units = units
        self.points = points
        self.immune = immune
        self.weak = weak
        self.damage = damage
        self.type = type
        self.initiative = initiative

    def power(self, boost):
        if self.army == "immune":
            return self.units * (self.damage + boost)
        else:
            return self.units * self.damage

def parse_line(line, army):
    m = re.match(r"(\d+) units each with (\d+) hit points (\(.+\) )?with an attack that does (\d+) ([a-z]+) damage at initiative (\d+)", line).groups()

    units, points, damage, type, initiative = int(m[0]), int(m[1]), int(m[3]), m[4], int(m[5])

    wi = m[2]
    weak = set()
    immune = set()
    if wi:
        wi = wi.strip(" ()").split(";")
        for i in wi:
            i = i.split()
            xx = set([x.strip(",") for x in i[2:]])
            if i[0] == "weak":
                weak = xx
            else:
                immune = xx
    return Group(army, units, points, immune, weak, damage, type, initiative)

def parse(inp, army):
    inp = inp.splitlines()
    inp = inp[1:]
    return map(lambda i: parse_line(i, army), inp)

def damage(attacker, defender, boost):
    dam = attacker.power(boost)
    if attacker.type in defender.immune:
        dam = 0
    if attacker.type in defender.weak:
        dam *= 2
    return dam

def fight(groups, boost):
    prev_imm = None
    prev_inf = None
    while True:
        # target selection
        groups = sorted(groups, key=lambda g: (-g.power(boost), -g.initiative))
        pairs = {}

        for attacker in groups:
            if attacker.units <= 0:
                continue
            defenders = list(filter(lambda g: g.army != attacker.army, groups))
            defenders = sorted(defenders, key=lambda d: (-damage(attacker, d, boost), -d.power(boost), -d.initiative))

            for defender in defenders:
                if defender not in pairs.values() and defender.units > 0 and damage(attacker, defender, boost) > 0:
                    pairs[attacker] = defender
                    break

        # attack
        groups = sorted(groups, key=lambda g: -g.initiative)
        for attacker in groups:
            if attacker.units == 0:
                continue
            if attacker not in pairs:
                continue

            defender = pairs[attacker]
            dead = damage(attacker, defender, boost) // defender.points

            dead = min(dead, defender.units)
            defender.units -= dead

        imm = sum([g.units for g in groups if g.army == "immune"])
        inf = sum([g.units for g in groups if g.army == "infect"])

        # can get stuck, escape
        if imm == prev_imm and inf == prev_inf:
            return None, None
        prev_imm, prev_inf = imm, inf
        if imm == 0 or inf == 0:
            return imm, inf

inp = sys.stdin.read().strip()
imm_inp, inf_inp = inp.split("\n\n")

groups = parse(imm_inp, "immune") + parse(inf_inp, "infect")

for boost in count():
    g = deepcopy(groups)
    imm, inf = fight(g, boost)
    if imm > 0:
        print(imm)
        break
