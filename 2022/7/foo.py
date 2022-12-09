import sys

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

class Dir:
    def __init__(self, parent):
        self.parent = parent
        self.dirs = []
        self.files = 0

    def size(self):
        return self.files + sum(d.size() for d in self.dirs)

root = Dir(None)
dirs = []

for x in xs:
    if x == "$ cd /":
        pwd = root
    elif x == "$ cd ..":
        pwd = pwd.parent
    elif x.startswith("$ cd"):
        parent = pwd
        pwd = Dir(pwd)
        parent.dirs.append(pwd)

        dirs.append(pwd)
    elif x == "$ ls":
        pass
    elif x.startswith("dir "):
        pass
    else:
        pwd.files += int(x.split()[0])

xx = sorted(dir.size() for dir in dirs)

print(sum(filter(lambda x: x < 1e5, xx)))

free = 7e7 - root.size()
to_free = 3e7 - free

print(list(filter(lambda x: x > to_free, xx))[0])
