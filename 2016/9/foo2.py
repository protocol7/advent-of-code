import sys

if len(sys.argv) > 1:
    inp = sys.argv[1]
else:
    inp = sys.stdin.read().strip()

inp = "".join(inp.split())

print("Slooooow on the real input")

i = 0
while i < len(inp):
    print(i, len(inp), len(inp) - i)
    c = inp[i]
    if c == "(":
        ni = inp.index(")", i)
        marker = inp[i+1:ni]
        l, times = [int(x) for x in marker.split("x")]
        sub = inp[ni+1:ni+1+l] * times
        inp = inp[:i] + sub + inp[ni+1+l:]
    else:
        i += 1

print(len(inp))
