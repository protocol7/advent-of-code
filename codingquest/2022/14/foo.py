import sys

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

gs = [
    ["keyless", "YYBBYYG"],
    ["society", "YGYYYBB"],
    ["phobias", "BBGBGBG"],
]

for guess, answer in gs:
    def matches(guess, answer, word):
        for i, (g, a) in enumerate(zip(guess, answer)):
            if a == "G":
                if not word[i] == g:
                    return False
            elif a == "B":
                if g in word:
                    return False
            elif a == "Y":
                if g not in word:
                    return False

        return True


    ns = []
    for x in xs:
        if matches(guess, answer, x):
            ns.append(x)

    xs = ns

assert len(xs) == 1
print(xs[0])
