target = 14

def foo(n, touchdown=False):
    if n <= 0:
        return [[]]

    ps = []

    if touchdown:
        ps.extend([p for p in foo(n)])

        ps.extend([p + [(1, "conversion")] for p in foo(n-1)])

        if n >= 2:
            ps.extend([p + [(2, "conversion")] for p in foo(n-2)])
    else:
        # safety is worth two points
        if n >= 2:
            ps.extend([p + [(2, "safety")] for p in foo(n-2)])
        if n >= 3:
            ps.extend([p + [(3, "field goal")] for p in foo(n-3)])
        if n >= 6:
            ps.extend([p + [(6, "touch-down")] for p in foo(n-6, True)])

    ps = set(tuple(sorted(p)) for p in ps)

    ps = [list(p) for p in ps]

    return ps

print(len(foo(14)))
print(len(foo(28)))
