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


def fibo3(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo3(n - 1) + fibo3(n - 2)


def fibo4(n, lt=None):
    if lt is None:
        lt = list()
        lt.append(0)
        lt.append(1)
    if n == 0:
        return lt[0]
    elif n == 1:
        return lt[1]
    else:
        lt.insert(n, fibo4(n - 1, lt) + fibo4(n - 2, lt))
        return lt[n]


fibo1(10)
fibo2(10)
fibo3(10)
fibo4(10)
