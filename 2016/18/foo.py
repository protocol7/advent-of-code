import sys

def row(prev):
    s = "." + prev + "."
    out = ""
    for i in range(len(prev)):
        l = s[i]
        c = s[i+1]
        r = s[i+2]
        if l == "^" and c == "^" and r == ".":
            out += "^"
        elif l == "." and c == "^" and r == "^":
            out += "^"
        elif l == "^" and c == "." and r == ".":
            out += "^"
        elif l == "." and c == "." and r == "^":
            out += "^"
        else:
            out += "."
    return out

first_row = sys.stdin.read().strip()
height = int(sys.argv[1])

rows = [first_row]
for r in range(height - 1):
    rows.append(row(rows[-1]))

count = 0
for row in rows:
    count += row.count(".")
print(count)
