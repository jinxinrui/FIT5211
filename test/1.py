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


def test(a, lt=None):
    lt = []
    lt.append(a)
    return lt


test(10)
test(100)

type(-100)
assert(1 != 1)
alist = [1, 2, 3]
len(alist)
# alist.append
blist = [3, 2, 1]

alist.append(blist)
len(alist)


for i in range(1, 2):
    print(i)


def fff(x=None):
    if x is None:
        x = []
    x.append(5)
    return x


fff()
