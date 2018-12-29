import sys

def parse(line):
    return line.strip()

def reset():
    return None, None, None

def tls(ip):
    hyper = False
    p1, p2, p3 = reset()
    found = False
    for c in ip:
        if c == "[":
            hyper = True
            p1, p2, p3 = reset()
        elif c == "]":
            hyper = False
            p1, p2, p3 = reset()
        else:
            if c == p3 and p1 == p2 and p1 != c:
                if hyper:
                    return False
                else:
                    found = True
            p3 = p2
            p2 = p1
            p1 = c
    return found


def ssl(ip):
    hyper = False
    p1, p2 = None, None
    found_outside = set()
    found_inside = set()
    for c in ip:
        if c == "[":
            hyper = True
            p1, p2 = None, None
        elif c == "]":
            hyper = False
            p1, p2 = None, None
        else:
            if c == p2 and p1 != c:
                if hyper:
                    found_inside.add(p1 + c + p1)
                else:
                    found_outside.add(c + p1 + c)
            p2 = p1
            p1 = c
    return len(found_inside.intersection(found_outside)) > 0

ips = map(parse, sys.stdin)

valid_tls = filter(tls, ips)
valid_ssl = filter(ssl, ips)

print(len(valid_tls))
print(len(valid_ssl))
