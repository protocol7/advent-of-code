import sys

if len(sys.argv) > 1:
    inp = sys.argv[1]
else:
    inp = sys.stdin.read().strip()

inp = "".join(inp.split())

i = 0
out = ""
while i < len(inp):
    c = inp[i]
    if c == "(":
        ni = inp.index(")", i)
        marker = inp[i+1:ni]
        l, times = [int(i) for i in marker.split("x")]
        out += inp[ni+1:ni+1+l] * times
        i = ni + l +1
    else:
        out += c
        i += 1

print(len(out))
