import sys
    
xs = sys.stdin.read().strip()

abc = []
with open("asciialphabet.txt") as f:
    for line in f:
        abc.append(line.strip("\n").ljust(6))

from string import ascii_uppercase

alphas = {}
for i, aa in zip(range(6, len(abc)+1, 6), ascii_uppercase):
    alphas[aa] = abc[i-6:i]

def count_spaces(s):
    t = 0
    for c in s:
        if c != " ":
            break
        t += 1
    return t

o = []
for x in xs:
    alpha = alphas[x]
    if not o:
        o = list(alpha)
    else:
        sp = []
        for i in range(6):
            # spaces at end of o
            oo = o[i][-10:]
            ospaces = count_spaces(oo[::-1])

            # spaces at begining ot a
            aspaces = count_spaces(alpha[i])

            sp.append((len(o[i]) - ospaces, ospaces + aspaces))

        delta = min(s for _, s in sp) - 1

        for i, (start, _) in zip(range(6), sp):
            if delta >= 0:
                o[i] += alpha[i]
                o[i] = o[i][:start] + o[i][start+delta:]
            elif delta == -1:
                o[i] += " " + alpha[i]

print(sum(line.count(" ") for line in o))