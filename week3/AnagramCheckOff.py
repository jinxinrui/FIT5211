# !/usr/local/bin/python3

from TestSuite import test


def checkOff(a, b):
    if len(a) != len(b):
        return False
    elif len(a) == 0 and len(b) == 0:
        return True
    elif a[0] not in list(b):
        return False
    else:
        blist = list(b)
        blist.remove(a[0])
        b = "".join(blist)
        return checkOff(a[1:], b)


test(checkOff("abc", "ba") is False)
test(checkOff("aaaabc", "abacaa") is True)
