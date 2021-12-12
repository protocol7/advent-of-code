import sys

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

s = 0
vs = []
for x in xs:
    
    st = []
    invalid = False
    for c in x:
        if c in "([{<":
            st.append(c)
        else:
            d = st.pop()

            if c == ")" and d != "(":
                s += 3
                invalid = True
            elif c == "]" and d != "[":
                s += 57
                invalid = True
            elif c == "}" and d != "{":
                s += 1197
                invalid = True
            elif c == ">" and d != "<":
                s += 25137
                invalid = True

            if invalid:
                break

    if not invalid:
        t = 0

        while st:
            t *= 5
            t += "([{<".index(st.pop()) + 1

        vs.append(t)

print(s)
print(sorted(vs)[len(vs) // 2])

    

