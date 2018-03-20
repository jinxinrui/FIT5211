# !/usr/local/bins/python3


def binary_search(l, v):
    lb = 0
    ub = len(l) - 1
    best = None
    while lb < ub:
        m = (lb + ub) // 2
        if (l[m] <= v):
            best = m
            lb = m + 1
        else:
            ub = m - 1
    return best
