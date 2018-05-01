# !/usr/local/bin/python3


def bestsublist(l):
    sublist = []
    if len(l) == 0:
        return sublist
    if len(l) == 1:
        return l
    else:
        mid = len(l) // 2
        alist = bestsublist(l[0:mid])
        # print(alist)
        blist = bestsublist(l[mid:len(l)])
        # print(blist)
        # sublist = alist + blist
        if alist[len(alist) - 1] == l[mid - 1] and blist[0] == l[mid]:
            if mid + 1 < len(l):
                clist = bestsublist(l[mid + 1:len(l)])
            else:
                clist = []
            if mid - 1 > 0:
                dlist = bestsublist(l[0:mid - 1])
            else:
                dlist = []
            if sum(blist) - sum(clist) >= sum(alist) - sum(dlist):
                alist = dlist
            else:
                blist = clist
        sublist = alist + blist
    return sublist


L = [1, 0, 5, 3, 2, 7, 9, 15, 6, 4, 13]
bestsublist(L)

a = [max(L) + 1 + i for i in L] + L
a
sum(bestsublist(a))
sum
