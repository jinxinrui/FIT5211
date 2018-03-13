# !/usr/local/bin/python3


import numpy as np
import time


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


def coingameImprove(n, dic=None):
    temp = np.array([0, 0])
    if dic is None:
        if n <= 4:
            dic = [None] * 4
        else:
            dic = [None] * n
        dic[0] = np.array([1, 1])
        dic[1] = np.array([1, 1])
        dic[2] = np.array([0, 2])
        dic[3] = np.array([1, 1]) + dic[2]
    if n == 1:
        return [dic[0], dic]
    elif n == 2:
        return [dic[1], dic]
    elif n == 3:
        return [dic[2], dic]
    elif n == 4:
        return [dic[3], dic]
    elif dic[n - 1] is not None:
        return [dic[n - 1], dic]
    else:
        res = np.array([1, 0]) + coingameImprove(n - 1, dic)[0]
        temp = calres(res, temp)
        res = np.array([1, 0]) + coingameImprove(n - 2, dic)[0]
        temp = calres(res, temp)
        res = np.array([1, 0]) + coingameImprove(n - 4, dic)[0]
        temp = calres(res, temp)
        dic[n - 1] = temp
        return [temp, dic]


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


start1 = time.time()
coingame(30)  # 1 means alice, 0 means Bob
end1 = time.time()
start2 = time.time()
coingameImprove(30)
end2 = time.time()
print("time: " + str(end1 - start1))

print("time: " + str(end2 - start2))
