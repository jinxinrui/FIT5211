# !/usr/local/bin/python3

# there is no n log n inplace mergeSort
#


def indexMergeSort(alist, temp=None, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(alist) - 1

    # if start == end:
    #     temp[start] = alist[start]
    if start < end:
        mid = (start + end) // 2
        indexMergeSort(alist, temp, start, mid)
        indexMergeSort(alist, temp, mid + 1, end)

        i = 0
        j = 0
        k = 0
        while i < (mid - start + 1) and j < (end - mid):
            if alist[start + i] < alist[mid + 1 + j]:
                temp[start + k] = alist[start + i]
                i = i + 1
            else:
                temp[start + k] = alist[mid + 1 + j]
                j = j + 1
            k = k + 1

        while i < (mid - start + 1):
            temp[start + k] = alist[start + i]
            i = i + 1
            k = k + 1

        while j < (end - mid):
            temp[start + k] = alist[mid + 1 + j]
            j = j + 1
            k = k + 1
        for i in range(start, end + 1):
            alist[i] = temp[i]
    # print("Merging ",alist)


temp = [None] * 15
alist = [2, 14, 80, 30, 12, 26, 34, 13, 75, 23, 13, 76, 21, 29, 100]
indexMergeSort(alist, temp)
alist
