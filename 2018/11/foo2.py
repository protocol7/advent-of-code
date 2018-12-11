serial = 7672

def value(x, y):
    rack_id = (x+1) + 10
    power = rack_id * (y+1)
    power += serial
    power *= rack_id
    power = (power // 100) % 10
    return power - 5

grid = [[value(x, y) for x in range(300)] for y in range(300)]

# hello laptop fans
largest = 0
for size in range(1, 301):
    for y in range(300 - (size - 1)):
        for x in range(300 - (size - 1)):
            total = 0
            for ys in range(size):
                for xs in range(size):
                    total += grid[y+ys][x+xs]
            if total > largest:
                largest = total

                print("%s,%s,%s" % (x+1, y+1, size))
