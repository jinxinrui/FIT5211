# !/usr/local/bins/python3


def recurse(n):
    print(n)
    if n > 1:
        recurse(n - 1)
        recurse(n // 2)


recurse(6)


def add(n=1):
    if n < 1e-10:
        return n
    return n + add(n / 3)**2 + add(n / 2)**2


add()
