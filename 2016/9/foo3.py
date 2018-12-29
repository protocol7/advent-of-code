import sys

if len(sys.argv) > 1:
    inp = sys.argv[1]
else:
    inp = sys.stdin.read().strip()

inp = "".join(inp.split())

def d(s):
    c = 0
    while "(" in s:
        start = s.index("(")
        end = s.index(")", start)

        marker = s[start+1:end]
        l, times = [int(x) for x in marker.split("x")]

        c += start
        c += d(s[end+1:end+1+l] * times)

        s = s[end+l+1:]
    c += len(s)
    return c

print(d(inp))
