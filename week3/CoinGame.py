# !/usr/local/bin/python3


import numpy as np


def coingame(n):
    # playerlist = ["bob", "alice"]
    temp = np.array([0, 0])
    if n == 1:
        res = np.array([1, 1])
        return res
    elif n == 2:
        res = np.array([1, 1])
        return res
    elif n == 3:
        res = np.array([0, 2])
        return res
    elif n == 4:
        res = np.array([1, 1]) + coingame(3)
        return res
    else:
        res = np.array([1, 0]) + coingame(n - 1)
        temp = calres(res, temp)
        res = np.array([1, 0]) + coingame(n - 2)
        temp = calres(res, temp)
        res = np.array([1, 0]) + coingame(n - 4)
        temp = calres(res, temp)
        return temp


def calres(res, temp):
    if res[0] % 2 == 1:
        if temp[0] == 1:
            temp[1] = res[1] + temp[1]
        else:
            temp[0] = 1
            temp[1] = res[1]
    else:
        if temp[0] == 0:
            temp[1] = res[1] + temp[1]
    return temp


coingame(4)  # 1 means alice, 0 means Bob
