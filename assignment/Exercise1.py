# !/usr/local/bin/python3


def F(n, l=None):
    if l is None:
        l = [None] * (n + 1)
    if n == 0:
        return 3
    elif n == 1:
        return 5
    elif n == 2:
        return 8
    if l[n] is not None:
        # print("in")
        return l[n]
    else:
        res = 2 * F(n - 2, l) + F(n - 3, l)
        l[n] = res
        return res


F(10)
