import sys

def parse(line):
    l = line.split()
    speed, runtime, resttime = int(l[3]), int(l[6]), int(l[-2])
    return Reindeer(speed, runtime, resttime)

class Reindeer():
    def __init__(self, speed, runtime, resttime):
        self.speed = speed
        self.runtime = runtime
        self.resttime = resttime
        self.state = "running"
        self.ran = 0
        self.rested = 0
        self.distance = 0
        self.points = 0

    def tick(self):
        if self.state == "running":
            if self.ran == self.runtime:
                self.state = "resting"
                self.ran = 0
                self.rested = 1
            else:
                self.ran += 1
                self.distance += self.speed
        elif self.state == "resting":
            if self.rested == self.resttime:
                self.state = "running"
                self.rested = 0
                self.ran = 1
                self.distance += self.speed
            else:
                self.rested += 1


rds = map(parse, sys.stdin)
rounds = int(sys.argv[1])

for tick in range(1, rounds+1):
    for rd in rds:
        rd.tick()
    best = max([rd.distance for rd in rds])
    for rd in rds:
        if rd.distance == best:
            rd.points += 1

print(max([r.points for r in rds]))
