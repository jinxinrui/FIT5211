# !/usr/local/bin/python3


def recursivelog(n, x, b, l=None, u=None):
    assert(n >= 0)
    assert(x >= 1)
    assert(isinstance(b, int))
    assert(b >= 2)

    if l == None:
        l = 0
    if u == None:
        u = x
    if n == 1:
        return (l + u) / 2
    else:
        mid = (l + u) / 2
        if b**mid == x:
            return mid
        elif b**mid > x:
            return recursivelog(n - 1, x, b, l, mid)
        else:
            return recursivelog(n - 1, x, b, mid, u)


recursivelog(100, 4, 2)
