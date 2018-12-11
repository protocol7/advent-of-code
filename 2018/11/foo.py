serial = 7672

def value(x, y):
    rack_id = (x+1) + 10
    power = rack_id * (y+1)
    power += serial
    power *= rack_id
    power = (power // 100) % 10
    return power - 5

grid = [[value(x, y) for x in range(300)] for y in range(300)]

largest = 0
largest_coord = None
for y in range(300 - 2):
    for x in range(300 - 2):
        total = 0
        for ys in range(3):
            for xs in range(3):
                total += grid[y+ys][x+xs]
        if total > largest:
            largest = total
            largest_coord = (x, y)

print(",".join([str(i+1) for i in largest_coord]))
