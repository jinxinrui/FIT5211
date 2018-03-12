# !/usr/local/bin/python3


def intersection(alist=[], blist=[]):
    aindex = 0
    bindex = 0
    res = []
    while aindex <= alist.size() or bindex <= blist.size():
        if alist[aindex] == blist[bindex]:
            res.append[alist[aindex]]
            aindex += 1
            bindex += 1
        else:
            if alist[aindex] > blist[bindex]:
                bindex += 1
            else:
                aindex += 1
    return res


def union(aSet, bSet):
    res = bSet
    for i in range(aSet.size()):
        if aSet[i] not in res:
            res.append(aSet[i])
    return res
