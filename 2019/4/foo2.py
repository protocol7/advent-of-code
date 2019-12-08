from collections import *

start = 264360
end = 746325

def f(i):
    s = str(i)
    return list(s) == sorted(s) and filter(lambda x: x == 2, Counter(s).values())

print(len(filter(f, range(start, end + 1))))
