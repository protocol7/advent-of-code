import sys

d = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

xs = sys.stdin.readlines()

t = 0
for x in xs:
    a = min((x.find(s), i) for s, i in d.items() if s in x)[1]
    b = max((x.rfind(s), i) for s, i in d.items() if s in x)[1]

    t += a * 10 + b

print(t)
