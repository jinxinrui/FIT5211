# !/usr/local/bin/python3

import random


def merge(left=[], right=[]):
    if not len(left) or not len(right):
        return left or right

    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break

    return result


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
    res2 = kthElementIt(a, b, k)
    if res1 != res2:
        assert(False)
    else:
        print("Correct!")


def kthElementIt(m, n, k):
    list = merge(m, n)
    return list[k - 1]


testQ5()
