# !/usr/local/bin/python3

from TestSuite import test
import random
import time


def matchIndexAndValueNonDistinct(lis=[], startindex=0):
    '''
    not distinct value in the list
    '''
    n = len(lis)
    if (n == 1) and (lis[0] != startindex):
        return False
    elif (n == 1) and (lis[0] == startindex):
        return True
    elif (lis[0] > n - 1) or (lis[n - 1] < startindex):
        return False
    else:
        mid = n // 2
        alis = lis[0:mid]
        blis = lis[mid:n]
        return (matchIndexAndValueNonDistinct(alis)
                or matchIndexAndValueNonDistinct(blis, mid))


def matchIndexAndValue(lis, startindex=None, lastindex=None):
    """
    distinct value in a sort list
    """
    n = len(lis)
    if startindex is None:
        startindex = 0
    if lastindex is None:
        lastindex = len(lis) - 1
    if n == 0:
        return False
    if startindex == lastindex:
        if lis[startindex] == startindex:
            return True
        else:
            return False
    else:
        mid = (startindex + lastindex) // 2
        if lis[mid] == mid:
            return True
        elif lis[mid] > mid:
            if mid == startindex:
                return False
            return matchIndexAndValue(lis, startindex, mid - 1)
        else:
            if mid == lastindex:
                return False
            return matchIndexAndValue(lis, mid + 1, lastindex)


def genq3(n, f):
    mem = set()
    if f % 2 == 0:
        idx = random.randint(0, n - 1)
        mem.add(idx)
        lhs, rhs = [], []
        while len(lhs) < idx:
            v = random.randint(0, idx - 1)
            if v in mem:
                continue
            mem.add(v)
            lhs.append(v)
        while len(rhs) < n - 1 - idx:
            v = random.randint(idx + 1, n)
            if v in mem:
                continue
            mem.add(v)
            rhs.append(v)
        lhs.sort()
        rhs.sort()
        return lhs + [idx] + rhs
    else:
        res = []
        while len(res) < n:
            v = random.randint(0, n)
            if v in mem:
                continue
            mem.add(v)
            res.append(v)
        return sorted(res)


def testq3():
    n = random.randint(1, 100)
    arr = genq3(n, random.randint(0, 3))
    # print(arr)
    res = matchIndexAndValue(arr)
    res2 = False
    for i in range(n):
        if i == arr[i]:
            res2 = True
    assert(res == res2)


a = [-1, 2]
matchIndexAndValue(a)


def testq3222():
    start = time.time()
    for i in range(1000000):
        testq3()
    end = time.time()
    return (end - start)


testq3222()
