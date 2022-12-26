import sys
from collections import *
from itertools import *
from util import *
from copy import deepcopy

xs = list(sys.stdin.read().strip())

#          222
#          222
#          222
#          up (U)
# 
# 333      111      444
# 333      111      444
# 333      111      444
# left(L) front(F) right(R)
# 
#          555
#          555
#          555
#          down(D)
# 
#          666
#          666
#          666
#          back(B)

cube = {
    1: [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
    2: [[2, 2, 2], [2, 2, 2], [2, 2, 2]],
    3: [[3, 3, 3], [3, 3, 3], [3, 3, 3]],
    4: [[4, 4, 4], [4, 4, 4], [4, 4, 4]],
    5: [[5, 5, 5], [5, 5, 5], [5, 5, 5]],
    6: [[6, 6, 6], [6, 6, 6], [6, 6, 6]],
}

def col(xs, c):
    return [row[c] for row in xs]

def row(xs, r):
    return xs[r][::]

def set_col(xs, c, vals):
    for i, v in enumerate(vals):
        xs[i][c] = v

def rotate_face(cube, face, clockwise):
    # rotate face
    face = cube[face]
    up = row(face, 0)
    mid = row(face, 1)
    down = row(face, 2)
    if clockwise:
        set_col(face, 2, up)
        set_col(face, 1, mid)
        set_col(face, 0, down)
    else:
        set_col(face, 0, up[::-1])
        set_col(face, 1, mid[::-1])
        set_col(face, 2, down[::-1])


def f(cube, clockwise):
    cube = deepcopy(cube)
    
    rotate_face(cube, 1, clockwise)

    # rotate sides
    up = row(cube[2], 2)
    right = col(cube[4], 0)
    down = row(cube[5], 0)
    left = col(cube[3], 2)

    if clockwise:
        set_col(cube[4], 0, up)
        cube[2][2] = left[::-1]
        set_col(cube[3], 2, down)
        cube[5][0] = right[::-1]
    else:
        set_col(cube[4], 0, down[::-1])
        cube[2][2] = right
        set_col(cube[3], 2, up[::-1])
        cube[5][0] = left

    return cube

def b(cube, clockwise):
    cube = deepcopy(cube)
    
    rotate_face(cube, 6, clockwise)

    # rotate sides
    up = row(cube[2], 0)
    right = col(cube[4], 2)
    down = row(cube[5], 2)
    left = col(cube[3], 0)

    if clockwise:
        set_col(cube[3], 0, up[::-1])
        cube[5][2] = left
        set_col(cube[4], 2, down[::-1])
        cube[2][0] = right
    else:
        set_col(cube[3], 0, down)
        cube[5][2] = right[::-1]
        set_col(cube[4], 2, up)
        cube[2][0] = left[::-1]

    return cube

def u(cube, clockwise):
    cube = deepcopy(cube)

    rotate_face(cube, 2, clockwise)    

    # rotate sides
    back = row(cube[6], 2)
    right = row(cube[4], 0)
    front = row(cube[1], 0)
    left = row(cube[3], 0)

    if clockwise:
        cube[4][0] = back[::-1]
        cube[1][0] = right
        cube[3][0] = front
        cube[6][2] = left[::-1]
    else:
        cube[4][0] = front
        cube[1][0] = left
        cube[3][0] = back[::-1]
        cube[6][2] = right[::-1]

    return cube

def d(cube, clockwise):
    cube = deepcopy(cube)
    
    rotate_face(cube, 5, clockwise)

    # rotate sides
    back = row(cube[6], 0)
    right = row(cube[4], 2)
    front = row(cube[1], 2)
    left = row(cube[3], 2)

    if clockwise:
        cube[4][2] = front
        cube[1][2] = left
        cube[3][2] = back[::-1]
        cube[6][0] = right[::-1]
    else:
        cube[4][2] = back[::-1]
        cube[1][2] = right
        cube[3][2] = front
        cube[6][0] = left[::-1]

    return cube

def l(cube, clockwise):
    cube = deepcopy(cube)
    
    rotate_face(cube, 3, clockwise)

    rotate_side(cube, 0, not clockwise)

    return cube

def r(cube, clockwise):
    cube = deepcopy(cube)
    
    rotate_face(cube, 4, clockwise)

    rotate_side(cube, 2, clockwise)

    return cube


def rotate_side(cube, index, direction):
    # rotate sides
    back = col(cube[6], index)
    up = col(cube[2], index)
    front = col(cube[1], index)
    down = col(cube[5], index)

    if direction:
        set_col(cube[1], index, down)
        set_col(cube[2], index, front)
        set_col(cube[6], index, up)
        set_col(cube[5], index, back)
    else:
        set_col(cube[1], index, up)
        set_col(cube[2], index, back)
        set_col(cube[6], index, down)
        set_col(cube[5], index, front)

i = 0
while i < len(xs):
    x = xs[i]

    if i+1 < len(xs):
        if xs[i+1] == "'":
            prime = True
            i += 1 
        else:
            prime = False

    if x == "R":
        cube = r(cube, not prime)
    elif x == "L":
        cube = l(cube, not prime)
    elif x == "U":
        cube = u(cube, not prime)
    elif x == "D":
        cube = d(cube, not prime)
    elif x == "F":
        cube = f(cube, not prime)
    elif x == "B":
        cube = b(cube, not prime)

    i += 1

p = 1
for row in cube[1]:
    for x in row:
        p *= x

print(p)