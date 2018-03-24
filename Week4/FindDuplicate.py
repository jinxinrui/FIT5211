# !/usr/local/bin/python3

from TestSuite import test


def merge(left=[], right=[]):
    if not len(left) or not len(right):
        return left or right

    result = []
    i, j = 0, 0
    lastelement = None
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            if lastelement != left[i]:
                result.append(left[i])
                lastelement = left[i]
            i += 1
        else:
            if lastelement != right[j]:
                result.append(right[j])
                lastelement = right[j]
            j += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break

    return result


def mergesort(list=[]):
    if len(list) < 2:
        return list

    middle = len(list) // 2
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])

    return merge(left, right)


def findDuplicate(list=[]):
    list = mergesort(list)
    return list


# def clean(list=[]):
#     res = []
#     if len(list) == 0:
#         return list
#     else:
#         res.append(list[0])
#     for i in range(len(list)):
#         list[i]
#     if list[i] == list[i + 1]:
#         list.pop(i)
#         clean(list, i)
#     else:
#         clean(list, i + 1)


a = [3, 1, 1, 10, 10, 1, 100, 20, 13, 30]
findDuplicate(a)
