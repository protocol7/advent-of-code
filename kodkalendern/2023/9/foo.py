import sys

x = sys.stdin.read().strip()

x = x.replace("/*", "").replace("-", "").replace("€", "").replace("*U", "")

print(len(x))

