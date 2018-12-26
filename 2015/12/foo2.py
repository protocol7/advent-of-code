import sys
import json

inp = sys.stdin.read()

j = json.loads(inp)

def e(n, sum):
    if isinstance(n, dict):
        for k, v in n.iteritems():
            if v == "red":
                return sum
        for k, v in n.iteritems():
            sum = e(v, sum)
    elif isinstance(n, int):
        sum += n
    elif isinstance(n, list):
        for v in n:
            sum = e(v, sum)
    elif isinstance(n, unicode):
        pass
    return sum

print(e(j, 0))
