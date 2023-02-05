sectors = [5, 20, 1, 18, 4, 13, 6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5, 20]

scores = []
for i in range(1, len(sectors) - 1):
    a, b, c = sectors[i-1:i+2]

    scores.append((a*0.25 + b*0.5 + c*0.25, b))

print(max(scores)[1])


# extra
def err(p):
    ps = p[-1:] + p + p[:1]

    xs = []
    for i in range(1, len(ps) - 1):
        a, b, c = ps[i-1:i+2]

        xs.append(a*0.25 + b*0.5 + c*0.25)

    avg = sum(xs) / len(xs)

    return sum(abs(x - avg) for x in xs)


best_error = 99999

xx = list(range(1, 21))
while True:
    # try to improve by swapping and picking the one with the least error
    xs = []
    for i in range(len(xx)):
        for j in range(len(xx)):
            ns = list(xx)
            ns[i], ns[j] = ns[j], ns[i]

            xs.append((err(ns), ns))

    e, ns = min(xs)

    if e >= best_error:
        break

    # print(e, ns)

    xx = ns
    best_error = e

print(xx)
