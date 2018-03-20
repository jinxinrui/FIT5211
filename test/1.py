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


mem = [None] * 3
mem[1] = 1
if mem[0] is None:
    print(mem[1])
print(mem)


ord("B")


def test(a, lt=None):
    lt = []
    lt.append(a)
    return lt


test(10)
test(100)
