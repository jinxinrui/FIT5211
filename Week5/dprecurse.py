# !/usr/local/bin/python3


def dp(n):
    l = [None] * (n + 1)
    l[0] = ""
    lines = 0
    for i in range(1, n + 1):
        l[i] = str(i) + '\n' + l[i - 1] + l[i // 2]
        # lines += 3
        # if i - 1 == 0:
        #     lines -= 1
        # if i // 2 == 0:
        #     lines -= 1
    return [l[n], lines]


def dplines(n):
    l = [[None, 0]] * (n + 1)
    l[0] = ["", 0]
    for i in range(1, n + 1):
        l[i][0] = str(i) + '\n' + l[i - 1][0] + l[i // 2][0]
        if i == 1:
            l[i][1] = l[i][1] + 1
        else:
            l[i][1] = l[i][1] + l[i - 1][1] + l[i // 2][1]
        print(l[i][1])
        if i - 1 == 0:
            l[i][1] -= 1
            print(l[i][1])
        if i // 2 == 0:
            l[i][1] -= 1
            print(l[i][1])
    return l[n]


dplines(6)
