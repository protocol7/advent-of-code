m=[*map(int,open(0))]
for p in 1,3:print(sum(map(int.__lt__,m,m[p:])))