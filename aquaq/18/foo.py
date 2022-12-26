import sys
import datetime

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

delta = datetime.timedelta(seconds=1)

def parse(ts):
    return datetime.datetime.strptime(ts, "%H:%M:%S")

def is_palindrome(ts):
    s = datetime.datetime.strftime(ts, "%H:%M:%S")
    return s == s[::-1]

s = 0
for x in xs:
    dt = parse(x)
    up = dt
    down = dt

    while not is_palindrome(up) and not is_palindrome(down):
        up = up + delta
        down = down - delta

    if is_palindrome(up):
        s += (up - dt).total_seconds()
    elif is_palindrome(down):
        s += (dt - down).total_seconds()

print(int(s))

    
