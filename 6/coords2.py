import sys

def parse(line):
    x, y = [int(i) for i in line.split(",")]
    return (x, y)

coords = map(parse, sys.stdin)

min_x, min_y, max_x, max_y = (sys.maxint, sys.maxint, 0, 0)
for x, y in coords:
    min_x = min(min_x, x)
    min_y = min(min_y, y)
    max_x = max(max_x, x)
    max_y = max(max_y, y)

def man_dist(x1, y1, x2, y2):
    return abs(x2-x1) + abs(y2-y1)

# find the number of locations that are within  a distance of each coordinate
locations = 0
for xs in range(min_x, max_x+1):
    for ys in range(min_y, max_y+1):
        dist = sum([man_dist(xs, ys, x, y) for (x, y) in coords])

        if dist < 10000:
            locations += 1

print(locations)
