# !/usr/local/bin/python3


import math
import numpy as np


def testType(n=int):
    return 1


testType(1)

n = 10
r = [[0, 0]] * n
print(r)

a = np.array([2, 1]) + np.array([1, 4])
print(a)
print(a[1])
print(type(np.array([2, 1])))


if res[0] % 2 == 1:
    if temp[0] == 1:
        temp[1] = res[1] + temp[1]
    else:
        temp[0] = 1
        temp[1] = res[1]
else:
    if temp[0] == 0:
        temp[1] = res[1] + temp[1]
