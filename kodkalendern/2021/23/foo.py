import sys
import re

for x in sys.stdin.read().split("\n"):
    if not re.match(r"1?2?3?4?5?6?7?8?9?[a-zä-ö]", x):
        print(x)