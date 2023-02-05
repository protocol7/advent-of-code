import random
import math

# simulate

# assume an R radius city
R = 100000

def randpoint():
    # https://stackoverflow.com/questions/30564015/how-to-generate-random-points-in-a-circular-distribution

    while True:
        # random angle
        a = 2 * math.pi * random.random()
        # random sqrt radius to give a uniform distribution
        r = R * math.sqrt(random.random())
        
        # calculating coordinates
        x = r * math.cos(a)
        y = r * math.sin(a)

        yield int(x), int(y)

drone = 0
scooter = 0
magic_scooter = 0

for x, y in randpoint():
    drone += math.sqrt(x*x + y*y)

    ax = abs(x)
    ay = abs(y)

    scooter += ax + ay

    if ax <= ay:
        magic_scooter += math.sqrt(2 * ax*ax) + (ay-ax)
    else:
        magic_scooter += math.sqrt(2 * ay*ay) + (ax-ay)

    print(scooter / drone, magic_scooter / drone)
