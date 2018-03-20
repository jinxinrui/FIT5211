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


def checkOffLinear(a, b):
    cnt1 = [0] * 256
    cnt2 = [0] * 256
    for i in a:
        cnt1[ord(i)] += 1
    for i in b:
        cnt2[ord(i)] += 1

    def compare(list1, list2):
        if len(list1) == 0 and len(list2) == 0:
            return True
        elif list1[len(list1) - 1] != list2[len(list2) - 1]:
            return False
        else:
            list1.pop()
            list2.pop()
            return compare(list1, list2)

    return compare(cnt1, cnt2)
    # return [cnt1[65], cnt2[65]]


# checkOffLinear("aaaabc", "abacaa")
test(checkOff("abc", "ba") is False)
test(checkOff("aaaabc", "abacaa") is True)
test(checkOffLinear("aaaabc", "abacaa") is True)
