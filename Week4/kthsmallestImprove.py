# !/usr/local/bin/python3


import random


def kthsmallestImprove(k, alist=[], blist=[], astart=None, aend=None, bstart=None, bend=None):
    """
    find the kth smallest element in the two sorted list
    """

    # initial the start and end point
    if astart is None:
        astart = 0
    if aend is None:
        aend = len(alist) - 1
    if bstart is None:
        bstart = 0
    if bend is None:
        bend = len(blist) - 1

    # base case
    if k == 0:
        return None
    if k > (len(alist) + len(blist)):
        return None
    if aend - astart < 0:
        return blist[bstart + k - 1]
    if bend - bstart < 0:
        return alist[astart + k - 1]
    if k == 1:
        if alist[astart] >= blist[bstart]:
            return blist[bstart]
        else:
            return alist[astart]

    amid = (aend + astart) // 2
    bmid = (bend + bstart) // 2
    # print("astart:" + str(astart))
    # print("aend:" + str(bend))
    # print("bstart:" + str(bstart))
    # print("bend:" + str(bend))
    # print("k:" + str(k))
    # print("alist[mid]:" + str(alist[amid]))
    # print("blist[mid]:" + str(blist[bmid]))
    if amid - astart + 1 + bmid - bstart + 1 <= k:
        if amid - astart + bmid - bstart + 2 == k and alist[amid] == blist[bmid]:
            return alist[astart]
        if alist[amid] > blist[bmid]:
            return kthsmallestImprove(k - (bmid - bstart) - 1, alist, blist, astart, aend, bmid + 1, bend)
        elif alist[amid] == blist[bmid]:
            return kthsmallestImprove(k - (bmid - bstart) - (amid - astart) - 2, alist, blist, amid + 1, aend, bmid + 1, bend)
        else:
            return kthsmallestImprove(k - (amid - astart) - 1, alist, blist, amid + 1, aend, bstart, bend)
    else:
        if alist[amid] > blist[bmid]:
            return kthsmallestImprove(k, alist, blist, astart, amid - 1, bstart, bend)
        elif alist[amid] == blist[bmid]:
            return kthsmallestImprove(k, alist, blist, astart, amid - 1, bstart, bmid - 1)
        else:
            return kthsmallestImprove(k, alist, blist, astart, aend, bstart, bmid - 1)


def testQ5():
    a = sorted([random.randint(0, 1000) for i in range(10)])
    b = sorted([random.randint(0, 1000) for i in range(10)])
    k = random.randint(1, len(a) + len(b))
    c = a + b
    c.sort()
    res1 = c[k - 1]
    print("a: ", a)
    print("b: ", b)
    print("k: ", k)
    res2 = kthsmallestImprove(k, a, b)
    if res1 != res2:
        assert(False)
    else:
        print("Correct!")


def test100Q5():

    for i in range(100):
        testQ5()


test100Q5()
