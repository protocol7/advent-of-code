import sys

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

s = 0
for x in xs:
    
    st = []
    for c in x:
        if c in "([{<":
            st.append(c)
        elif c in ")]}>":

            d = st.pop()

            if c == ")" and d != "(":
                s += 3
                break
            elif c == "]" and d != "[":
                s += 57
                break
            elif c == "}" and d != "{":
                s += 1197
                break
            elif c == ">" and d != "<":
                s += 25137
                break


print(s)