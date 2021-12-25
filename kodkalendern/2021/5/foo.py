i = 0
a = 1
s = 0

while i < 100:
    s += i    
    i += a
    a = 1 if a == 7 else 7

print(s)