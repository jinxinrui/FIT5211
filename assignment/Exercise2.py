# !/usr/local/bin/python3


def e_approx(n, i=1):
    if i == n:
        return 1 + 1 / n
    else:
        return 1 + e_approx(n, i + 1) / i


e_approx(100)
