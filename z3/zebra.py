import z3

# There are five houses.
# The Englishman lives in the red house.
# The Spaniard owns the dog.
# Coffee is drunk in the green house.
# The Ukrainian drinks tea.
# The green house is immediately to the right of the ivory house.
# The Old Gold smoker owns snails.
# Kools are smoked in the yellow house.
# Milk is drunk in the middle house.
# The Norwegian lives in the first house.
# The man who smokes Chesterfields lives in the house next to the man with the fox.
# Kools are smoked in the house next to the house where the horse is kept.
# The Lucky Strike smoker drinks orange juice.
# The Japanese smokes Parliaments.
# The Norwegian lives next to the blue house.

s = z3.Solver()

nationalities = ("englishman", "japanese", "ukrainian", "norwegian", "spaniard")
animals = ("dog", "snails", "horse", "fox", "zebra")
drinks = ("coffee", "milk", "oj", "tea", "water")
colors = ("blue", "red", "yellow", "green", "ivory")
smokes = ("oldgolds", "kools", "parliaments", "chesterfields", "luckystrikes")

vars = {}

for v in nationalities + animals + drinks + colors + smokes:
    vars[v] = z3.Int(v)

    s.add(vars[v] >= 1, vars[v] <= 5)

s.add(z3.Distinct(*[vars[v] for v in nationalities]))
s.add(z3.Distinct(*[vars[v] for v in animals]))
s.add(z3.Distinct(*[vars[v] for v in drinks]))
s.add(z3.Distinct(*[vars[v] for v in colors]))
s.add(z3.Distinct(*[vars[v] for v in smokes]))

# The Englishman lives in the red house.
s.add(vars["englishman"] == vars["red"])

# The Spaniard owns the dog.
s.add(vars["spaniard"] == vars["dog"])

# Coffee is drunk in the green house.
s.add(vars["green"] == vars["coffee"])

# The Ukrainian drinks tea.
s.add(vars["ukrainian"] == vars["tea"])

# The green house is immediately to the right of the ivory house.
s.add(vars["green"] - vars["ivory"] == 1)

# The Old Gold smoker owns snails.
s.add(vars["oldgolds"] == vars["snails"])

# Kools are smoked in the yellow house.
s.add(vars["kools"] == vars["yellow"])

# Milk is drunk in the middle house.
s.add(vars["milk"] == 3)

# The Norwegian lives in the first house.
s.add(vars["norwegian"] == 1)

# The man who smokes Chesterfields lives in the house next to the man with the fox.
s.add(z3.Or(vars["chesterfields"] - vars["fox"] == 1, vars["fox"] - vars["chesterfields"] == 1))

# Kools are smoked in the house next to the house where the horse is kept.
s.add(z3.Or(vars["kools"] - vars["horse"] == 1, vars["horse"] - vars["kools"] == 1))

# The Lucky Strike smoker drinks orange juice.
s.add(vars["luckystrikes"] == vars["oj"])

# The Japanese smokes Parliaments.
s.add(vars["japanese"] == vars["parliaments"])

# The Norwegian lives next to the blue house.
s.add(z3.Or(vars["norwegian"] - vars["blue"] == 1, vars["blue"] - vars["norwegian"] == 1))


assert s.check() == z3.sat

m = s.model()

print("Who drinks water?")
for v in nationalities:
    if m[vars[v]] == m[vars["water"]]:
        print(v)

print("Who owns the Zebra?")
for v in nationalities:
    if m[vars[v]] == m[vars["zebra"]]:
        print(v)
