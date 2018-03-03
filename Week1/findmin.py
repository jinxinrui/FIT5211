# !/usr/local/bin/python3
import time
from random import randrange


def findMin(alist):
    overallmin = alist[0]
    for i in alist:
        issmallest = True
        for j in alist:
            if i > j:
                issmallest = False
        if issmallest:
            overallmin = i
    return overallmin


findMin([5, 3, 1, 10, 2])


for listSize in range(1000, 10001, 1000):
    alist = [randrange(100000) for x in range(listSize)]
    start = time.time()
    print(findMin(alist))
    end = time.time()
    print("size: %d time: %f" % (listSize, end - start))
