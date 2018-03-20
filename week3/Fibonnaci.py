# !/usr/local/bin/python3


def fibo1(n):
    filist = list()
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        filist.append(0)
        filist.append(1)
        for i in range(n - 1):
            res = filist[i] + filist[i + 1]
            filist.append(res)
        return filist[n]


def fibo2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        res = 0
        for i in range(n - 1):
            res = a + b
            a = b
            b = res
        return res


def fibo3(n, lt=None):
    # if lt is None:
    #     lt = [None] * n
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo3(n - 1) + fibo3(n - 2)


def fibo4(n, lt=None):
    if lt is None:
        lt = [None] * (n + 1)
        lt[0] = 0
        lt[1] = 1
    if n == 0:
        return [lt[0], lt]
    elif n == 1:
        return [lt[1], lt]
    elif lt[n] is not None:
        return [lt[n], lt]
    else:
        res = fibo4(n - 1, lt)[0] + fibo4(n - 2, lt)[0]
        lt[n] = res
        return [lt[n], lt]


fibo1(10)
fibo2(10)
fibo3(10)
fibo4(100)[0]
