row = 2981
column = 3075

def val(column, row, i, fn):
    diagonal = column + row
    for d in range(1, diagonal + 1):
        for r in range(d, 0, -1):
            c = d - (r-1)
            if r == row and c == column:
                return i
            i = fn(i)

def v(prev):
    return (prev * 252533) % 33554393

print(val(column, row, 20151125, v))
