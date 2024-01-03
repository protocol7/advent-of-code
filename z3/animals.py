import z3

# Spend exactly 100 dollars and buy exactly 100 animals.
# Dogs cost 15 dollars, cats cost 1 dollar, and mice cost 25 cents each.
# You have to buy at least one of each. How many of each should you buy?

dogs, cats, mice = z3.Ints("dogs cats mice")

s = z3.Solver()

s.add(dogs + cats + mice == 100)
s.add(dogs * 15 + cats + mice * 0.25 == 100)
s.add(dogs > 0)
s.add(cats > 0)
s.add(mice > 0)

print(s.check())

print(s.model())
