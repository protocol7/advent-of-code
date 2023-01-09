
def trib(a, b, c):
    while True:
        a, b, c = b, c, a + b + c

        if c > 2023:
            break

        yield c

def run(n):
    for a in range(1, n):
        for b in range(a, n):
            for c in range(b, n):
                # since we're looking for the smallest sum of a, b and c, we can break once we find the first match
                if n in trib(a, b, c):
                    return a, b, c

print(run(2023))